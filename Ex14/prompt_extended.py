from sys import argv

script, user_name, job_title = argv
prompt = '''Please enter your response here, I'm waiting:

     (~'~~'~~'~~)
      |        |
      |        |
      |       ~|~                         _ __
      |-------())                        ||  |
      (        _)                      .'~\  /.
      |        |                     ()()__\/ ".
      |        |                     /*        "
      ''..     |                     |     //  |
      |'..'---_/\                    |    ()   |
     /    ''---|| /\                 ".       ."
    /     \    \\/\/                   "..  ."\\
    |  \  /     \_/                      || |  ^
    |   \/\\    | \-ABG                 ((__)-ABG

==================================================
> '''

prompt_2 = '> '

print 'Hi %s-%s, I\'m the %s script.' % (user_name, job_title, script)
print 'I\'d like to ask you a few questions.'
print 'Do you like me, %s?' % user_name
likes = raw_input(prompt)

print 'Where do you live, %s?' % user_name
lives = raw_input(prompt_2)

print 'What kind of computer do you have?'
computer = raw_input(prompt_2)

print '''
Which operating system do you fancy?
Type (1) for Mac OSX
Type (2) for Windows
Type (3) for Linux (any distro)
'''
fav_os = int(raw_input(prompt))

if fav_os == 1:
    print 'Hey, excellent choice!'
elif fav_os == 2:
    print 'Have you read the EULA - comical!'
elif fav_os == 3:
    print '3l33tH4x0r4Lif3'

print '''
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
''' % (likes, lives, computer)
