def convert_to_yolo(x1, y1, x2, y2, img_width, img_height):
    # 바운딩 박스 중심 계산
    cx = (x1 + x2) / 2.0
    cy = (y1 + y2) / 2.0
    
    # 바운딩 박스 너비와 높이 계산
    w = x2 - x1
    h = y2 - y1
    
    # YOLO 형식으로 변환 (이미지 크기 대비 상대 좌표)
    cx /= img_width
    cy /= img_height
    w /= img_width
    h /= img_height
    
    return cx, cy, w, h

# 예시 좌표
x1, y1 = 100, 150  # 좌측 상단 좌표
x2, y2 = 200, 300  # 우측 하단 좌표
img_width = 500
img_height = 500

# YOLO 포맷으로 변환
cx, cy, w, h = convert_to_yolo(x1, y1, x2, y2, img_width, img_height)
print(f"YOLO 포맷: 중심 ({cx}, {cy}), 너비 {w}, 높이 {h}")
