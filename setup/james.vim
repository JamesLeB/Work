set background=dark
hi clear
if exists("syntax_on")
	syntax reset
endif
let g:colors_name = "james"

hi normal		ctermfg=darkgreen
hi comment 		ctermfg=darkred
hi constant 	ctermfg=gray
hi special 		ctermfg=green
hi identifier 	ctermfg=darkcyan
hi statement 	ctermfg=darkgreen
hi preproc 		ctermfg=blue
hi type 		ctermfg=darkgreen
hi underlined	ctermfg=darkgreen
hi error 		ctermfg=white
hi matchparen   ctermfg=darkgreen ctermbg=gray
hi LineNr 		ctermfg=darkgreen
hi javaScript	ctermfg=darkgreen
"source $VIMRUNTIME/syntax/hitest.vim
"black,gray,white,red,greeb,blue,yellow,cyan,magenta