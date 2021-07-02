import cv2

img_paths = (
    '/home/zhenyue-qin/Pictures/tall/Screenshot from 2021-07-02 22-09-26.png',
    '/home/zhenyue-qin/Pictures/tall/Screenshot from 2021-07-02 22-09-35.png',
    '/home/zhenyue-qin/Pictures/tall/Screenshot from 2021-07-02 22-09-42.png',
    '/home/zhenyue-qin/Pictures/tall/Screenshot from 2021-07-02 22-09-49.png',
    '/home/zhenyue-qin/Pictures/tall/Screenshot from 2021-07-02 22-09-58.png',
    '/home/zhenyue-qin/Pictures/tall/Screenshot from 2021-07-02 22-10-06.png'
)

idx_ = 0
for an_img_path in img_paths:
    an_img = cv2.imread(an_img_path)
    an_img = an_img[110:, :, :]
    cv2.imwrite('tmp_{}.png'.format(idx_), an_img)
    idx_ += 1
