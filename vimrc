syntax on 
set number 
set noswapfile 
set hlsearch
set ignorecase
set incsearch


"""""""""""""""""""""""""""""""""""""vim.plug"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

call plug#begin('~/.vim/plugged')
Plug 'sheerun/vim-polyglot'
Plug 'dense-analysis/ale'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'jiangmiao/auto-pairs'
Plug 'jaredgorski/spacecamp'
call plug#end()




"""""""""""""""""""""""""""""""""""""coc.nvim"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

inoremap <expr> <cr> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"
inoremap <silent><expr> <cr> pumvisible() ? coc#_select_confirm() : "\<C-g>u\<CR>"
inoremap <silent><expr> <cr> pumvisible() ? coc#_select_confirm() : "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"
if exists('*complete_info')
  inoremap <silent><expr> <cr> complete_info(['selected'])['selected'] != -1 ? "\<C-y>" : "\<C-g>u\<CR>"
endif

" use <tab> for trigger completion and navigate to the next complete item
function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~ '\s'
endfunction

inoremap <silent><expr> <Tab>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<Tab>" :
      \ coc#refresh()

inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"

autocmd FileType json syntax match Comment +\/\/.\+$+




""""""""""""""""""""""""""""""""""""""template"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

nnoremap <F9> :r /home/keju/.vim/template/html.html




"""""""""""""""""""""""""""""""""""""colorscheme"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
colorscheme spacecamp

"""""""""""""""""""""""""""""""""""""colorscheme"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
inoremap jk <ESC>
