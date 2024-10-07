import re


def is_email(email : str) -> bool:
    return bool(re.search(r"^[a-zA-Z0-9!#$%&'*+\-/=?^_`{|}~]+(\.[a-zA-Z0-9!#$%&'*+\-/=?^_`{|}~]+)*@([a-zA-Z]+\.)+(com|se|org|net)$", email))


test_emails = ["test@mail.com",
               "double.test@hotmail.se",
               "my.name53@student.school.net",
               "should-not.not-work@us.org",
               "should.work@us.org",
               "no",
               "start1.middle2@end3.com",
               "name.domain.se",
               "@hotmail.com",
               "uh.oh@",
               "oh.no.this.is.long@and.stupid",
               "so.close@yet.so.far.de",
               ".bad.email@nono.com",
               "also.bad.@uhuh.net"]

for email in test_emails:
    print(f"{email} -> {is_email(email)}")