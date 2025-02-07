from __future__ import division

from model import *
from utils import *
from kitti_dataset import KITTI

from terminaltables import AsciiTable
import time, datetime

import torch
from torch.utils.data import DataLoader
from torch.autograd import Variable
import torch.optim as optim

if __name__ == "__main__":

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    fp = open("dataset/classes.names", "r")
    class_names = fp.read().split("\n")[:-1]

    # Initiate model
    model = COMPLEXYOLO("config/complex_yolov3.cfg", img_size=608).to(device)
    model.apply(weights_init_normal)

    dataset = KITTI('dataset',split='train',mode='TRAIN',folder='training')
    dataloader = DataLoader(dataset,4,shuffle=True,num_workers=8,pin_memory=True,collate_fn=dataset.collate_fn)
    optimizer = torch.optim.Adam(model.parameters())

    metrics = ["grid_size","loss","x","y","w","h","im","re","conf","cls","cls_acc","recall50","recall75","precision","conf_obj","conf_noobj"]

    max_mAP = 0.0
    for epoch in range(0, 300):
        model.train()
        start_time = time.time()

        for batch_i, (_, imgs, targets) in enumerate(dataloader):
            batches_done = len(dataloader) * epoch + batch_i

            imgs = Variable(imgs.to(device))
            targets = Variable(targets.to(device), requires_grad=False)

            loss, outputs = model(imgs, targets)
            loss.backward()

            if batches_done % 2:
                # Accumulates gradient before each step
                optimizer.step()
                optimizer.zero_grad()

            log_str = "\n---- [Epoch %d/%d, Batch %d/%d] ----\n" % (epoch, 300, batch_i, len(dataloader))

            metric_table = [["Metrics", *[f"YOLO Layer {i}" for i in range(len(model.yolo_layers))]]]

            # Log metrics at each YOLO layer
            for i, metric in enumerate(metrics):
                formats = {m: "%.6f" for m in metrics}
                formats["grid_size"] = "%2d"
                formats["cls_acc"] = "%.2f%%"
                row_metrics = [formats[metric] % yolo.metrics.get(metric, 0) for yolo in model.yolo_layers]
                metric_table += [[metric, *row_metrics]]

            log_str += AsciiTable(metric_table).table
            log_str += f"\nTotal loss {loss.item()}"

            # Determine approximate time left for epoch
            epoch_batches_left = len(dataloader) - (batch_i + 1)
            time_left = datetime.timedelta(seconds=epoch_batches_left * (time.time() - start_time) / (batch_i + 1))
            log_str += f"\n---------- ETA {time_left}"

            print(log_str)

            model.seen += imgs.size(0)

            torch.save(model.state_dict(), f"checkpoints/jkjas-%d.pth" % (epoch))




