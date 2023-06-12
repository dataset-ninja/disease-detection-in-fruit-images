# https://github.com/QuIIL/Dataset-Region-Aggregated-Attention-CNN-for-Disease-Detection-in-Fruit-Images

import os
import xml.etree.ElementTree as ET

import numpy as np
from tqdm import tqdm

import supervisely as sly
from supervisely.io.fs import get_file_name


def convert_and_upload_supervisely_project(api: sly.Api, workspace_id, project_name):
    dataset_path = "/Users/almaz/Downloads/Dataset-Region-Aggregated-Attention-CNN-for-Disease-Detection-in-Fruit-Images-main"
    ds_name = "ds0"
    batch_size = 30
    download_bbox = True

    def create_ann(image_path):
        labels = []
        image_np = sly.imaging.image.read(image_path)[:, :, 0]
        image_name = get_file_name(image_path)
        mask_path = os.path.join(masks_path, image_name + "_mask.png")

        ann_np = sly.imaging.image.read(mask_path)[:, :, 0]
        unique_idx = list(np.unique(ann_np))
        unique_idx.remove(0)
        for idx in unique_idx:
            mask = ann_np == idx
            curr_bitmap = sly.Bitmap(mask)
            curr_label = sly.Label(curr_bitmap, obj_class)
            labels.append(curr_label)

        if download_bbox is True:
            coords = []
            bbox_path = os.path.join(bbox_pathes, image_name + "_d.xml")

            tree = ET.parse(bbox_path)
            root = tree.getroot()
            coords_xml = root.findall(".//Pt")
            for coord in coords_xml:
                text_coord = coord.text.split(",")
                coords.append(list(map(float, text_coord)))
            for i in range(0, len(coords), 4):
                min_x_coord = min(coords[i][0], coords[i + 1][0])
                max_x_coord = max(coords[i][0], coords[i + 1][0])
                min_y_coord = min(coords[i][1], coords[i + 2][1])
                max_y_coord = max(coords[i][1], coords[i + 2][1])
                curr_rectangle = sly.Rectangle(
                    top=min_y_coord, left=min_x_coord, bottom=max_y_coord, right=max_x_coord
                )
                curr_label = sly.Label(curr_rectangle, obj_class_bbox)
                labels.append(curr_label)

        return sly.Annotation(img_size=(image_np.shape[0], image_np.shape[1]), labels=labels)
    YELLOW_COLOR = [255, 255, 0]
    GREEN_COLOR = [15, 138, 125]

    obj_class = sly.ObjClass("anthracnose", sly.Bitmap, color=GREEN_COLOR)
    obj_class_collection = sly.ObjClassCollection([obj_class])
    if download_bbox is True:
        obj_class_bbox = sly.ObjClass("anthracnose_bbox", sly.Rectangle, color=YELLOW_COLOR)
        obj_class_collection = sly.ObjClassCollection([obj_class, obj_class_bbox])

    project_info = api.project.create(workspace_id, project_name)

    meta = sly.ProjectMeta(obj_classes=obj_class_collection)
    api.project.update_meta(project_info.id, meta.to_json())

    dataset = api.dataset.create(project_info.id, ds_name, change_name_if_conflict=True)

    images_path = os.path.join(dataset_path, "Images")
    images_names = os.listdir(images_path)
    masks_path = os.path.join(dataset_path, "Labels_mask")
    bbox_pathes = os.path.join(dataset_path, "Labels_xml")

    progress = tqdm(desc=f"Create dataset {ds_name}", total=len(images_names))

    for images_names_batch in sly.batched(images_names, batch_size=batch_size):
        img_pathes_batch = [
            os.path.join(images_path, image_name) for image_name in images_names_batch
        ]

        anns_batch = [create_ann(image_path) for image_path in img_pathes_batch]

        img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        api.annotation.upload_anns(img_ids, anns_batch)

        progress.update(len(images_names_batch))

    return project_info
