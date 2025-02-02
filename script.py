from pathlib import Path
from wordcloud import WordCloud
from pathlib import Path
import random
import matplotlib.pyplot as plt

def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 70%%, %d%%)" % random.randint(20, 60)

if __name__ == '__main__':

    data_file = Path.cwd().joinpath('words.txt')
    data = data_file.read_text().lower()

    wc = WordCloud(background_color=None, random_state=1, width=300, height=200).generate(data)
    plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
           interpolation="bilinear")

    outfile = Path(__file__).parent.joinpath('cloud.svg')

    with outfile.open(mode='w') as out:
        svg = wc.to_svg(embed_font=True)
        out.write(svg)
