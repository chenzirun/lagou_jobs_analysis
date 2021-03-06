from wordcloud import WordCloud, ImageColorGenerator
import matplotlib.pyplot as plt
import jieba

import dy

df = dy.con_sql('job')

text = ''
for line in df['job_welfare']:
    text += ' '.join(jieba.cut(line, cut_all=False))
backgroud_Image = plt.imread('1.PNG')

wc = WordCloud(
    background_color='white',
    mask=backgroud_Image,
    font_path='/Users/goodbyekiller/Library/Fonts/SimHei.ttf',
    max_words=2000,
    max_font_size=150,
    random_state=30,
)
wc.generate_from_text(text)
img_colors = ImageColorGenerator(backgroud_Image)
wc.recolor(color_func=img_colors)
plt.imshow(wc)
plt.axis('off')
wc.to_file("福利.jpg")
print('生成词云成功!')