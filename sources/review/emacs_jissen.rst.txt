=============
emacs実践入門
=============

MEMO
====

ターミナル環境へのインストール
-------------------------------
% wget http://ftp.gnu.org/pb/emacs/emacs-23.4.tar.gz
% tar xvf emacs-23.4.tar.gz &&  cd  emacs-23.4
% ./configure --without-x && make && make install

デーモン起動・終了
------------------

::

    % emacs --daemon
    %  emacsclient -n or emacsclient  -nw
    % emacsclient  -e '(kill-emacs)'






その他Tips
-----------

- align-regexp
