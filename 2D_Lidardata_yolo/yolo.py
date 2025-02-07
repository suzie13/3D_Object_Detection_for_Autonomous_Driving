import torch.nn as nn
import torch.nn.functional as F
import torch
from torch.autograd import Variable


class COMPLEXYOLO(nn.Module):
    def __init__(self):
        super(COMPLEXYOLO, self).__init__()
        self.conv_1 = nn.Conv2d(in_channels=3,out_channels=24,kernel_size=3,stride=1,padding=1)
        self.bn_1   = nn.BatchNorm2d(num_features=24)
        self.pool_1 = nn.MaxPool2d(2)

        self.conv_2 = nn.Conv2d(in_channels=24,out_channels=48,kernel_size=3,stride=1,padding=1)
        self.bn_2   = nn.BatchNorm2d(num_features=48)
        self.pool_2 = nn.MaxPool2d(2)

        self.conv_3 = nn.Conv2d(in_channels=48,out_channels=64,kernel_size=3,stride=1,padding=1)
        self.bn_3   = nn.BatchNorm2d(num_features=64)
        self.conv_4 = nn.Conv2d(in_channels=64,out_channels=32,kernel_size=1,stride=1,padding=0)
        self.bn_4   = nn.BatchNorm2d(num_features=32)
        self.conv_5 = nn.Conv2d(in_channels=32,out_channels=64,kernel_size=3,stride=1,padding=1)
        self.bn_5   = nn.BatchNorm2d(num_features=64)
        self.pool_3 = nn.MaxPool2d(2)

        self.conv_6 = nn.Conv2d(in_channels=64,out_channels=128,kernel_size=3,stride=1,padding=1)
        self.bn_6   = nn.BatchNorm2d(num_features=128)
        self.conv_7 = nn.Conv2d(in_channels=128,out_channels=64,kernel_size=3,stride=1,padding=1)
        self.bn_7   = nn.BatchNorm2d(num_features=64)
        self.conv_8 = nn.Conv2d(in_channels=64,out_channels=128,kernel_size=3,stride=1,padding=1)
        self.bn_8   = nn.BatchNorm2d(num_features=128)
        self.pool_4 = nn.MaxPool2d(2)

        self.conv_9  = nn.Conv2d(in_channels=128,out_channels=256,kernel_size=3,stride=1,padding=1)
        self.bn_9    = nn.BatchNorm2d(num_features=256)
        self.conv_10 = nn.Conv2d(in_channels=256,out_channels=256,kernel_size=1,stride=1,padding=0)
        self.bn_10   = nn.BatchNorm2d(num_features=256)
        self.conv_11 = nn.Conv2d(in_channels=256,out_channels=512,kernel_size=3,stride=1,padding=1)
        self.bn_11   = nn.BatchNorm2d(num_features=512)
        self.pool_5  = nn.MaxPool2d(2)

        self.conv_12 = nn.Conv2d(in_channels=512,out_channels=512,kernel_size=3,stride=1,padding=1)
        self.bn_12   = nn.BatchNorm2d(num_features=512)
        self.conv_13 = nn.Conv2d(in_channels=512,out_channels=512,kernel_size=1,stride=1,padding=0)
        self.bn_13   = nn.BatchNorm2d(num_features=512)
        self.conv_14 = nn.Conv2d(in_channels=512,out_channels=1024,kernel_size=3,stride=1,padding=1)
        self.bn_14   = nn.BatchNorm2d(num_features=1024)
        self.conv_15 = nn.Conv2d(in_channels=1024,out_channels=1024,kernel_size=3,stride=1,padding=1)
        self.bn_15   = nn.BatchNorm2d(num_features=1024)
        self.conv_16 = nn.Conv2d(in_channels=1024,out_channels=1024,kernel_size=3,stride=1,padding=1)
        self.bn_16   = nn.BatchNorm2d(num_features=1024)

        self.conv_17 = nn.Conv2d(in_channels=2048,out_channels=1024,kernel_size=3,stride=1,padding=1)
        self.bn_17   = nn.BatchNorm2d(num_features=1024)
        self.conv_18 = nn.Conv2d(in_channels=1024,out_channels=75,kernel_size=1,stride=1,padding=0)

        self.relu = nn.ReLU(inplace=True)
        self.conv2_drop = nn.Dropout2d(p = 0.2)


    def forward(self,x):
        # print("before conv1",x.shape)
        # x = self.relu(self.conv_1(x))
        # print("after conv1",x.shape)
        # x = self.pool_1(x)
        # print("after pool1",x.shape)
        # x = self.relu(self.conv_2(x))
        # print("after conv2",x.shape)
        # x = self.pool_2(x)
        # print("after pool2",x.shape)

        # x = self.relu(self.conv_3(x))
        # print("after conv3",x.shape)
        # x = self.relu(self.conv_4(x))
        # print("after conv4",x.shape)
        # x = self.relu(self.conv_5(x))
        # print("after conv5",x.shape)
        # x = self.pool_3(x)
        # print("after pool3",x.shape)
        # x = self.relu(self.conv_6(x))
        # print("after conv6",x.shape)
        # x = self.conv2_drop(x)
        # print("after drop",x.shape)
        # x = self.relu(self.conv_7(x))
        # print("after conv7",x.shape)
        # x = self.relu(self.conv_8(x))
        # print("after conv8",x.shape)
  
        
        # x = self.relu(self.conv_9(x))
        # print("after conv9",x.shape)

        # x = self.relu(self.conv_10(x))
        # print("after conv10",x.shape)
        # x = self.relu(self.conv_11(x))
        # print("after conv11",x.shape)

        # x = self.relu(self.conv_12(x))
        # print("after conv12",x.shape)
        # x = self.relu(self.conv_13(x))
        # print("after conv13",x.shape)
        # x = self.relu(self.conv_14(x))
        # print("after conv14",x.shape)
        # x = self.relu(self.conv_15(x))
        # print("after conv15",x.shape)
        # x = self.relu(self.conv_16(x))
        # print("after conv16",x.shape)
        # x = self.pool_4(x)
        # print("after pool4",x.shape)
        # x = self.relu(self.conv_17(x))
        # print("after conv17",x.shape)
        # x = self.relu(self.conv_18(x))
        # print("after conv18",x.shape)
        # x = self.relu(self.conv_19(x))
        # print("after conv19",x.shape)
        # x = self.relu(self.conv_20(x))
        # print("after conv20",x.shape)
        # x = self.relu(self.conv_21(x))
        # print("after conv21",x.shape)
        # x = self.relu(self.conv_22(x))
        # print("after conv22",x.shape)
        # x = self.relu(self.conv_23(x))
        # print("after conv23",x.shape)
        # x = self.conv_24(x)
        # print("after conv24",x.shape)
        x = self.relu(self.bn_1(self.conv_1(x)))
        print("after conv1", x.shape)
        x = self.pool_1(x)
        
        x = self.relu(self.bn_2(self.conv_2(x)))
        x = self.pool_2(x)

        x = self.relu(self.bn_3(self.conv_3(x)))
        x = self.relu(self.bn_4(self.conv_4(x)))
        x = self.relu(self.bn_5(self.conv_5(x)))
        x = self.pool_3(x)

        x = self.relu(self.bn_6(self.conv_6(x)))
        x = self.relu(self.bn_7(self.conv_7(x)))
        x = self.relu(self.bn_8(self.conv_8(x)))
        x = self.pool_4(x)
        
        x = self.relu(self.bn_9(self.conv_9(x)))
        r = x            # 12 layer
        reorg_result = reorg(r)
        
        x = self.relu(self.bn_10(self.conv_10(x)))
        x = self.relu(self.bn_11(self.conv_11(x)))
        x = self.pool_5(x)

        x = self.relu(self.bn_12(self.conv_12(x)))
        x = self.relu(self.bn_13(self.conv_13(x)))
        x = self.relu(self.bn_14(self.conv_14(x)))
        x = self.relu(self.bn_15(self.conv_15(x)))
        x = self.relu(self.bn_16(self.conv_16(x)))

        x = torch.cat((reorg_result,x),1)
        x = self.relu(self.bn_17(self.conv_17(x)))
        x = self.conv_18(x)

        return x
def reorg(x):

        B, C, H, W = x.shape
        x = x.view(B, C, int(H/2), 2, int(W/2), 2).transpose(3,4).contiguous()
        x = x.view(B, C, int(H/2*W/2), 2*2).transpose(2,3).contiguous()
        x = x.view(B, C, 2*2, int(H/2), int(W/2)).transpose(1,2).contiguous()
        x = x.view(B, 2*2*C, int(H/2), int(W/2))

        return x

"""
after pool1 torch.Size([12, 24, 256, 512])
after conv2 torch.Size([12, 48, 256, 512])
after pool2 torch.Size([12, 48, 128, 256])
after conv3 torch.Size([12, 64, 128, 256])
after conv4 torch.Size([12, 32, 128, 256])
after conv5 torch.Size([12, 64, 128, 256])
after pool3 torch.Size([12, 64, 64, 128])
after conv6 torch.Size([12, 128, 64, 128])
after drop torch.Size([12, 128, 64, 128])
after conv7 torch.Size([12, 64, 64, 128])
after conv8 torch.Size([12, 128, 64, 128])
after pool4 torch.Size([12, 128, 32, 64])
after conv9 torch.Size([12, 256, 32, 64])
after conv10 torch.Size([12, 256, 32, 64])
after conv11 torch.Size([12, 512, 32, 64])
after pool5 torch.Size([12, 512, 16, 32])
after conv12 torch.Size([12, 512, 16, 32])
after conv13 torch.Size([12, 512, 16, 32])
after conv14 torch.Size([12, 1024, 16, 32])
after conv15 torch.Size([12, 1024, 16, 32])
after conv16 torch.Size([12, 1024, 16, 32])
after conv17 torch.Size([12, 1024, 16, 32])
after conv18 torch.Size([12, 75, 16, 32])
"""


######With new one###

# before conv1 torch.Size([12, 3, 512, 1024])
# after conv1 torch.Size([12, 64, 256, 512])
# after pool1 torch.Size([12, 64, 128, 256])
# after conv2 torch.Size([12, 192, 128, 256])
# after pool2 torch.Size([12, 192, 64, 128])
# after conv3 torch.Size([12, 128, 64, 128])
# after conv4 torch.Size([12, 256, 64, 128])
# after conv5 torch.Size([12, 256, 64, 128])
# after pool3 torch.Size([12, 256, 32, 64])
# after conv6 torch.Size([12, 512, 32, 64])
# after drop torch.Size([12, 512, 32, 64])
# after conv7 torch.Size([12, 256, 32, 64])
# after conv8 torch.Size([12, 512, 32, 64])
# after conv9 torch.Size([12, 256, 32, 64])
# after conv10 torch.Size([12, 512, 32, 64])
# after conv11 torch.Size([12, 256, 32, 64])
# after conv12 torch.Size([12, 512, 32, 64])
# after conv13 torch.Size([12, 256, 32, 64])
# after conv14 torch.Size([12, 512, 32, 64])
# after conv15 torch.Size([12, 512, 32, 64])
# after conv16 torch.Size([12, 1024, 32, 64])
# after pool4 torch.Size([12, 1024, 16, 32])
# after conv17 torch.Size([12, 512, 16, 32])
# after conv18 torch.Size([12, 1024, 16, 32])
# after conv19 torch.Size([12, 512, 16, 32])
# after conv20 torch.Size([12, 1024, 16, 32])
# after conv21 torch.Size([12, 1024, 16, 32])
# after conv22 torch.Size([12, 1024, 8, 16])
# after conv17 torch.Size([12, 1024, 8, 16])
# after conv18 torch.Size([12, 1024, 8, 16])


# Traceback (most recent call last):
#   File "D:\Complex-YOLO\main.py", line 45, in <module>
#     loss = region_loss(output,target)
#   File "C:\Users\sushm\.conda\envs\pytorch_gpu\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
#     return forward_call(*input, **kwargs)
#   File "D:\Complex-YOLO\region_loss.py", line 117, in forward
#     prediction = x.view(nB, nA, self.bbox_attrs, nH, nW).permute(0, 1, 3, 4, 2).contiguous()  # prediction [12,5,16,32,15]
# RuntimeError: shape '[12, 5, 15, 8, 16]' is invalid for input of size 1572864
