import smtplib
from dotenv import load_dotenv
import os
load_dotenv()
email_from = 'daniils.panasyuk@yandex.ru'
email_to = 'ivand650@gmail.com'
message = """
From:{0}
 To: {1} 
 Subject: Приглашение! 
 Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
""".format(email_from, email_to)
message = message.replace("%website%", "https://dvmn.org/profession-ref-program/ivand650/DVBWt/")
message = message.replace("%friend_name%", "Игорь")
message = message.replace("%my_name%", "Ибрагим")
message = message.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login((os.environ['login']), (os.environ['password']))
server.sendmail(email_from, email_to, message)
server.quit() 

