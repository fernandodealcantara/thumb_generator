Script para gerar thumbnails simples

Para utilizar o menu para gerar thumbnails utilize:\
python script.py 

Para utilizar a linha de comando para gerar thumbnails utilize:\
python script.py -U 

Exemplo:\
python script.py -U -i node.jpg -t Node -n 5 -x 0.70 -y 0.20 -st 170 -sn 300 -C -I 4

As thumbnails geradas são salvas no diretório thumbs/

Help command\
python script -h

usage: Thumbnail generator [-h] \
[-i {responsividade.jpg,html_css.jpg,apresentacao.jpg,git_github.jpg,node.jpg,react.jpg,bd.jpg,javascript.jpg}] \
[-t TEXT] \
[-n NUMBER] \
[-x COORX] \
[-y COORY] \
[-st FONTSIZETEXT] \
[-sn FONTSIZENUMBER] \
[-I ITERATOR] \
[-U] \
[-C]

Avaliable arguments thumb generator 

options: \
  -h, --help            show this help message and exit \
  -i {responsividade.jpg,html_css.jpg,apresentacao.jpg,git_github.jpg,node.jpg,react.jpg,bd.jpg,javascript.jpg}, --image {responsividade.jpg,html_css.jpg,apresentacao.jpg,git_github.jpg,node.jpg,react.jpg,bd.jpg,javascript.jpg} \
                        Image file (include image format) \
  -t TEXT, --text TEXT  Image text \
  -n NUMBER, --number NUMBER \
                        Image number \
  -x COORX, --coorX COORX \
                        Text X position (between 0 and 1) \
  -y COORY, --coorY COORY\
                        Text Y position (between 0 and 1)\
  -st FONTSIZETEXT, --fontSizeText FONTSIZETEXT\
                        Font size text\
  -sn FONTSIZENUMBER, --fontSizeNumber FONTSIZENUMBER\
                        Font size number\
  -I ITERATOR, --Iterator ITERATOR\
                        Quantity of thumbs to generate\
  -U, --useArgs         Should be informed to enable command line args.\
  -C, --clearOutputDir  Remove all thumbs in output dir before add new ones.
