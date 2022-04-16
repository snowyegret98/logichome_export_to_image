from PIL import Image
import os


def discern_bit(data):
    if data == "0":
        return img_0
    elif data == "1":
        return img_1


def main(filename):
    filename = filename[:-4]
    with open(f"input/{filename}.txt", "r") as f:
        lines = f.readlines()
        lines = [i.strip() for i in lines if i != "\n"]

    logic_width, logic_height, logic_data = int(lines[1]), int(lines[2]), lines[3]
    canvas_width, canvas_height = logic_width * img_0_width, logic_height * img_0_height

    width_point = [(i * img_0_width) for i in range(logic_width)]
    height_point = [(i * img_0_height) for i in range(logic_height)]

    with Image.new("RGB", (canvas_width, canvas_height), (255, 255, 255)) as canvas:
        i = 0
        for hei in height_point:
            for wid in width_point:
                canvas.paste(discern_bit(logic_data[i]), (wid, hei))
                i += 1
        canvas.save(f"output/{filename}.png")


img_0 = Image.open("0.png")
img_0_width = int(img_0.size[0])
img_0_height = int(img_0.size[1])

img_1 = Image.open("1.png")
img_1_width = int(img_1.size[0])
img_1_height = int(img_1.size[1])

if img_0_width != img_1_width or img_0_height != img_1_height:
    print("에러: 0.png와 1.png의 크기가 다릅니다.")
    print("0.png의 크기와 1.png의 크기는 같아야 합니다.")
    input("종료하려면 엔터를 누르세요.")
    exit(1)

for name in os.listdir("./input"):
    if name.endswith(".txt"):
        main(name)
        print(f"[작업 완료] {name}")

input("\n작업이 완료되었습니다.\n종료하시려면 엔터를 누르세요.")
