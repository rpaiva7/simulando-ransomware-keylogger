## RANSOMWARE
## Executando o script de Ransonware

### 1º - Altere o tipo de Terminal para o PowerShell no VS Code

![powershell](https://i.imgur.com/tosh8oY.jpeg)

&nbsp;

2º - Instale a biblioteca Fernet através do Terminal do VS Code para poder executar o Ransomware e criptografar os arquivos

O Fernet é uma biblioteca de criptografia autenticada simétrica para Python. Simétrica porque usa a mesma chave para criptografar e descriptografar, simplificando o processo para o usuário. 

Comando: python -m pip install cryptography

![fernet](https://i.imgur.com/RmOhAbz.jpeg)


3º - Abra o Terminal do VS Code e digite o comando abaixo:

Comando: python .\nomedoarquivo.py

![ransomware](https://i.imgur.com/LmiwmoM.jpeg)

Pronto! Os arquivos estarão criptografados. 


4º - Descriptografando os arquivos

Criar um novo arquivo na pasta MALWARE do VS Code que vamos chamar de descriptografar.py, inserir nele o código ransomware e rodar o código no terminal através do comando abaixo

Comando: python .\descriptografar.py

![antes](https://i.imgur.com/Wn7dVAJ.jpeg)

![depois](https://i.imgur.com/3QK3ogv.jpeg)


KEYLOGGER

Um keylogger é um tipo de malware que registra secretamente todos os toques de teclado de um usuário, permitindo que um invasor roube informações confidenciais como senhas, números de cartão de crédito e dados pessoais. Eles podem ser baseados em software (mais comuns, instalados via malware) ou em hardware (dispositivos físicos). Os principais objetivos são espionar e roubar dados, mas os keyloggers também podem ser usados para outros fins, como monitoramento de funcionários ou para recuperar o histórico de digitação.


5º - Abrindo uma nova pasta chamada Keylogger no VS Code e instalando a biblioteca pynput com o comando abaixo.

Comando: python -m pip install pynput

![]()

O pip é um gerenciador de pacotes do Python que nos permite instalar novas bibliotecas e funcionalidades dentro da instalação padrão do Python no computador.

O pynput é uma biblioteca Python que pode ser usada dentro do VS Code para controlar e monitorar o teclado e o mouse.


6º - Criando o código do Keylogger

1 - Crie o arquivo keylogger.py dentro da pasta KEYLOGGER no VS Code.
2 - Dentro desse arquivo importe o keyboard da biblioteca pynput
3 - Escreva o código
4 - Rode o comando abaixo no terminal shell do VS Code para confirmar se deu certo:

Comando: python .\keylogger.py

![]()

Ao digitar textos aleatórios em navegadores e aplicativos diferentes, conseguimos visualizar que o ataque deu certo, que o arquivo log.txt foi criado automaticamente no VS Code e que tudo que estou digitando está sendo capturado e salvo instantaneamente neste arquivo.

![]()

7º - Tornando o Keylogger invisível para o usuário

Ao alterarmos a extensão do nossa arquivo .py para .pyw conseguimos deixar o Keylogger invisível para o usuário. No Windows, os arquivos .pyw são scripts Python que rodam em segundo plano, sem abrir o terminal, e é uma funcionalidade nativa do Python no Windows.

Para alterarmos, basta rodarmos o comando abaixo no terminal shell do VS Code dentro da pasta onde está o Keylogger, ou então alterar manualmente renomeando o arquivo.

Comando: ren .\keylogger.py .\keylogger.pyw 

![]()

Na sequência devemos rodar o script novamente. Ele agirá silenciosamente e irá capturar tudo o que digitarmos e salvará no arquivo log.txt. É assim que os ataques acontecem na prática. 

Comando: 

![]()

8º - Enviando remotamente os dados capturados para o atacante

1 - Criar um gmail apenas para testes como esse
2 - Ativar a verificação em duas etapas e criar uma senha de app exlusiva nesse gmail para o aplicativo python para ser inserida em nosso código malicioso. É uma senha exclusiva para envio de e-mails via aplicativo. Essa é uma etapa comum em malwares reais para exportação dos dados para outro lugar sem chamar a atenção da vítima.

Como usar a senha exclusiva de app?

Acesse as configurações da sua Conta do Google no aplicativo ou dispositivo que você está tentando configurar. Substitua sua senha pela senha de 16 caracteres mostrada acima. Assim como sua senha normal, esta senha de app concede acesso total à sua Conta do Google. Não é necessário memorizá-la, por isso não a anote ou a compartilhe com outras pessoas.

3 - Ativar no terminal Powershell do VS Code a bibliotecas smtplib para o ataque. Ela já vem no Python por padrão, mas se não estiver é só rodar o comando abaixo para instalá-la.

Comando: python -m pip install secure-smtplib

4 - Na pasta KEYLOGGER do VS Code, criar um novo arquivo chamado keylogger_email onde será escrito o código malicioso.

5 - Após a escrita do código malicioso, rodamos o ataque com o comando abaixo e aguardamos 60 segundos para recebermos no e-mail tudo o que foi digitado pela vítima neste intervalo de tempo. 

Comando: python .\keylogger_email.py

![]()

![]()


Detectando e prevenindo ameaças

Para detectar e prevenir ameaças de malware como keyloggers e ransomware, é crucial adotar uma abordagem de segurança em várias camadas. Nenhuma ferramenta ou método único oferece proteção total, mas a combinação de práticas recomendadas e ferramentas de segurança pode reduzir significativamente o risco. Alguns métodos que podem ser adotados são: 

- Mantenha o Software Atualizado: A maioria dos ataques explora vulnerabilidades em software desatualizado. Mantenha seu sistema operacional (Windows, macOS, Linux), navegadores e todos os outros programas atualizados com os patches de segurança mais recentes.

- Use um Software Antivírus/Antimalware Confiável: Instale e mantenha um programa de segurança robusto e que seja executado em tempo real. Soluções modernas oferecem proteção contra vírus, ransomware e spyware (incluindo keyloggers).

- Habilite o Firewall: Um firewall monitora o tráfego de rede de entrada e saída, bloqueando conexões não autorizadas que malwares tentam estabelecer.

- Evite Phishing: Desconfie de e-mails, mensagens ou ligações que solicitem informações pessoais ou financeiras, ou que criem um senso de urgência incomum.

- Tenha Cautela com Anexos e Links: Nunca clique em links suspeitos nem abra anexos de e-mails de remetentes desconhecidos ou inesperados.

- Baixe de Fontes Oficiais: Instale software apenas de sites oficiais ou lojas de aplicativos confiáveis para evitar pacotes de instalação maliciosos. 

- Escaneamentos Regulares: Configure seu software antivírus para realizar varreduras completas do sistema regularmente.

- Monitoramento de Comportamento: Soluções de segurança modernas usam análise comportamental para detectar atividades suspeitas (como um programa tentando criptografar centenas de arquivos rapidamente, típico de ransomware, ou registrar teclas, típico de keyloggers) e bloquear a ameaça mesmo que ela seja nova.

- Backup, Backup, Backup: Esta é a defesa mais crítica. Mantenha cópias de segurança regulares de todos os seus dados importantes em um local seguro e offline (como um disco rígido externo desconectado após o backup ser concluído) ou em um serviço de nuvem confiável com versões de arquivo. Se for atacado, você pode simplesmente limpar o sistema e restaurar seus arquivos.

- Ambientes isolados para testes: utilização de máquinas virtuais para limitar os riscos.

- Segmente a Rede: Em ambientes corporativos, isole sistemas críticos e evite que o ransomware se espalhe facilmente para outras máquinas.

- Autenticação de Dois Fatores (2FA): Mesmo que um keylogger capture sua senha, o 2FA (ou MFA) impede o acesso à conta, pois o invasor não terá o segundo código temporário.

- Use um Gerenciador de Senhas: Gerenciadores de senhas preenchem automaticamente os campos de login, reduzindo a necessidade de digitar suas credenciais manualmente e mitigando a eficácia dos keyloggers baseados em digitação.

- Teclado Virtual: Para logins muito sensíveis (como em bancos), use o teclado virtual oferecido pelo próprio site, se disponível.

- Ferramentas Anti-Keylogger específicas: Existem programas projetados especificamente para criptografar as teclas que você digita ou alertá-lo sobre software de monitoramento de teclado.
