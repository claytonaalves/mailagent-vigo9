A versão 9 do sistema Vigo não trabalha corretamente com o MySQL em versões menores
que a 5.5, dessa forma foi necessário criar este esquema para sincronizar as contas
de email criadas no Vigo9 com um servidor de emails remoto rodando uma versão
inferior do MySQL.

As triggers são utilizadas para disparar eventos de inserção, atualização e remoção
de emails no servidor remoto através do script mailagent.py.

