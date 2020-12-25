# 

## server ip

- 192.168.8.124:80
- 192.168.1.22:80

## /stream_fire_predict

```
input: 
        {
            image: bytes
        }
    return:
        {
            bboxes: [[xmin, ymin, xmax, ymax], ...], bbox_list
            confidences[float, ...]
        }
```



## /bbox/numpy_bboxes_filter

```
input: 
        {
            image: bytes
        }
    return:
        {
            bboxes: [[xmin, ymin, xmax, ymax], ...], bbox_list
            confidences[float, ...]
        }
```



## /bbox/get_fire_patches

```
将明火ssd检测后的框框进行整合和裁减，形成新的bboxes
    input:
        image_bytes:
        bbox_list:
        box_heigh_thres:
        aspect_ratio_thres:
    output:
        dst_bbox_list:
```



## /bbox/rectangle_bbox_lsit

```
将输入的矩形，在图像范围内根据长边剪切为正方形
    input:
        bbox_list: list, [[xmin, ymin, xmax, ymax], ... ]
        img_hw: list or tuple, [height, width]
    output:
        [[xmin, ymin, xmax, ymax], ... ]
```



## /bbox/upscale_bbox_lsit

```
bbox按照尺度放大
    input:
        bboxes_list: [[xmin, ymin, xmax, ymax], ... ]
        img_hw: list or tuple, [height, width]
        scale: float
    output:
        upscaled_bboxes_list: [[xmin, ymin, xmax, ymax], ... ]
```



## /stream_fire_ts_classify -- OK 

```json
input:
        image_bytes: list, [image_bytes, image_bytes, ...], 6张图片
output:
        
```



## /person/get_persons -- ok

```json
input: 
    {image: bytes}

    return:
        {
            bboxes: [[xmin, ymin, xmax, ymax], ...], bbox_list
            confidences[[float], ...]
        }
```



## /person/get_head_leg_body -- ok

```json
input: 
        {
            image: bytes, required
            original_bbox: [[xmin, ymin, xmax, ymax]...], bbox that obtained by person_detector
        }
    return:
        {   
            bboxes: {
                head: [xmin, ymin, xmax, ymax],
                body: [xmin, ymin, xmax, ymax],
                leg: [xmin, ymin, xmax, ymax]
            }
            confidences: {
                head: float,
                body: float,
                leg: float
            }

            
        }
```



## /person/classify_helmet -- ok

```json
input: 
        {
            image: bytes, required
            thr: float, optional， 阈值, default = 0.5
        }
    return:
        {
            labels: [[xmin, ymin, xmax, ymax], ...]
            confidences: [float, ...]
        }
```

## /person/service_det_helmet -- ok

```json
检测安全帽业务
    input: 
        
            image: bytes
        
    return:
        {
            bboxes: [
                    [xmin, ymin, xmax, ymax], 
                    ...
                    ], bbox_list
            resluts:[
                    {'labels': 'long-hair', 'confidences': 0.27301687002182007},
                    {'labels': 'soft-hat', 'confidences': 0.27301687002182007},
                    ...
                    ]
        }
```

