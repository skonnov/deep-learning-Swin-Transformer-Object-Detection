# pip install mmcv-full==1.4.0
# git clone https://github.com/SwinTransformer/Swin-Transformer-Object-Detection
# cd Swin-Transformer-Object-Detection-master
# pip install -r requirements/build.txt
# pip install -v -e .
# wget http://download.openmmlab.com/mmdetection/v2.0/mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth

from mmdet.apis import inference_detector, init_detector
import cv2 as cv
import time

# config_file = r'C:\swin\configs\mask_rcnn\mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco.py'
# checkpoint_file = r'C:\swin\weights\mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'

# config_file = r'C:\swin\configs\faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'
# checkpoint_file = r'C:\swin\weights\faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'

# if with CPU，you need to replace "SyncBN" with "BN" in config_file
config_file = r'Swin-Transformer-Object-Detection/configs/mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco.py'
checkpoint_file = r'mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'


model = init_detector(config_file, checkpoint_file, device='cpu')# cuda:0

def detect(img):
    result = inference_detector(model, img)
    return model.show_result(
                img,
                result,
                score_thr=.5,
                show=False,
                wait_time=0,
                win_name='result',
                bbox_color=(72, 101, 241),
                text_color=(72, 101, 241)
    )
 
if __name__ == "__main__":
    img_path = r"Swin-Transformer-Object-Detection/demo/demo.jpg"
    image = cv.imread(img_path)
 
    start = time.time() 
    image = detect(image)
    end = time.time()
    print(end-start)

    cv.imwrite('result.jpg', image)
    # cv.waitKey(0)
    # cv.destroyAllWindows()