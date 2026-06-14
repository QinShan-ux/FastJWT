from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `clas` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL COMMENT '班级名称'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `sno` INT NOT NULL COMMENT '学号',
    `pwd` VARCHAR(255) NOT NULL COMMENT '密码',
    `name` VARCHAR(255) NOT NULL COMMENT '姓名',
    `clas_id` INT NOT NULL,
    CONSTRAINT `fk_student_clas_4be9b492` FOREIGN KEY (`clas_id`) REFERENCES `clas` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `teacher` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL COMMENT '姓名',
    `tno` INT NOT NULL COMMENT '账号',
    `pwd` VARCHAR(255) NOT NULL COMMENT '密码'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `course` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL COMMENT '课程名',
    `teacher_id` INT NOT NULL COMMENT '课程讲师',
    CONSTRAINT `fk_course_teacher_2de38fe7` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student_course` (
    `student_id` INT NOT NULL,
    `course_id` INT NOT NULL,
    FOREIGN KEY (`student_id`) REFERENCES `student` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_student_cou_student_0d222b` (`student_id`, `course_id`)
) CHARACTER SET utf8mb4 COMMENT='学生选课表';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztWW1vmzAQ/isVnzqpm8gLDdm3NFu1rmsrtd00qa2QAUNQiJ2CWRtV/Pf5BYIhwEjT5m"
    "XKlzS9O5u75853D86LMsE29MNPQx+EyueDFwWBCaRfcvKjAwVMp5mUCQgwfW5opRZmSAJg"
    "ESpzgB9CKrJhaAXelHgYUSmKfJ8JsUUNPeRmogh5jxE0CHYhGcGAKu4eqNhDNnyGYfrvdG"
    "w4HvTtnJuezZ7N5QaZTbnsDJFTbsieZhoW9qMJyoynMzLCaG7tIcKkLkQwAASy7UkQMfeZ"
    "d0mUaUTC08xEuCitsaEDIp9I4TbEwMKI4Ue9EXlw2VM+tlvdXlfvHHd1asI9mUt6sQgvi1"
    "0s5Ahc3iox1wMChAWHMcON/11AbjgCQTl0qX0BPOpyEbwUqjr0UkEGX1Yytfgp91GvA236"
    "CUHvPtK6Kvved1SlGaoT8Gz4ELlkxKDUtBoMfw2uh98G14fU6gPbHdPiFhV/majaQhfHrD"
    "qdsYQzE5jAGj+BwDZymiwDIYlsyPxayMJJsvL0/Br6gEe+iHxyPm/ELmtNQuMijtMqSqXJ"
    "OeGA4TauQmxRNWlPihKAgMu9Zs9mT0o7Fo6CEJb2MqGp72aZzb6f7fvZGvqZbjqQ9jCgmq"
    "KfbbSTHUmlSCCwaPUaS5VkftG/S3Od6Oqm2aYYQ1VviPEb1OzCaFjAdxHcUxxAz0XncMYx"
    "PqNOAWSVlWvS2G6znXYF26rRQMUBeJo3xkI90dBpwJCIwz24GQ6+fFXi6mm74pxpMqwvAJ"
    "rdYvbZMFkrTOxXNmmaKs08Pqap0lrOfdRX1X6aPF0/Xj1hPDCjMGylMAPGYqA9txAzVmCJ"
    "A56JMZxJMCfZnucp0Yp1iZKMAhy5I3lVNrtL64TKjeJUjGupRBpDCZeQwqsmE6FktGcTO8"
    "QmQoSXAC6x3vywE6dc6zi99Q04mTFMn0rqrZqDJeabp2CaabHuqKutrSFfu8tntb7d2TIm"
    "y66olqOx0ooNH+u19sQatppe861IVdP7xO3DrykjlUpjY3RUZlCrsdHsTuR/JqNZlEUumi"
    "P2eTKao5tFLppnqquTUQ5vPRtN3/JK2Kj0AljNRqX3zT0b3bbOW8dG91zgLW+1lqL2ZFuo"
    "vW6399R+d6n9q34hqpzyy/xA9PoBv21Xg+/6q9EABp41KputiaZ2tILMZj9Zd2iy/oFBmJ"
    "yepp1NWrLh7tYcxfefquxoLAFiYr6bALZUtQGA1KoSQK4rXFFgRJKr4jyI32+uLivuKLIl"
    "BSB/Ihrgne1Z5OjA90LysJ2w1qDIomZOT8Lw0ZfBO7wY/C7iOvxxdcJRwCFxA74L3+Bkuc"
    "H79uMl/gsV1vbl"
)
