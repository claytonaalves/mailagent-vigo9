drop trigger InsereContaEmail;
drop trigger AtualizaContaEmail;
drop trigger RemoveContaEmail;
drop procedure ExecutaComandoEmail;

DELIMITER ^

CREATE PROCEDURE ExecutaComandoEmail(Comando VARCHAR(3), Email VARCHAR(80), Password VARCHAR(20), Quota BigInt(20))
BEGIN
    DECLARE ExitCode INTEGER;
    DECLARE cmd VARCHAR(180);
    SET cmd = CONCAT_WS(' ', '/usr/local/bin/mailupdater.py', Comando, Email, Password, CAST(Quota AS CHAR));
    SELECT sys_exec(cmd) INTO ExitCode;
END^

CREATE TRIGGER InsereContaEmail 
AFTER INSERT ON users 
FOR EACH ROW
BEGIN
    CALL ExecutaComandoEmail('ins', NEW.email, NEW.password, NEW.quota);
END^

CREATE TRIGGER AtualizaContaEmail
AFTER UPDATE ON users 
FOR EACH ROW
BEGIN
    CALL ExecutaComandoEmail('upd', NEW.email, NEW.password, NEW.quota);
END^

CREATE TRIGGER RemoveContaEmail
BEFORE DELETE ON users 
FOR EACH ROW
BEGIN
    CALL ExecutaComandoEmail('del', OLD.email, OLD.password, OLD.quota);
END^

DELIMITER ;


insert into users (id, email) values (5, 'clayton.aa@gmail.com');
