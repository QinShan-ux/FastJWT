from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `teacher` (
    `name` VARCHAR(100) NOT NULL,
    `age` INT NOT NULL,
    `address` VARCHAR(100) NOT NULL,
    `account` VARCHAR(100) NOT NULL,
    `password` VARCHAR(100) NOT NULL,
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `course` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(255) NOT NULL COMMENT '课程名',
    `teacher_id` INT NOT NULL COMMENT '课程讲师',
    CONSTRAINT `fk_course_teacher_2de38fe7` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
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
    "eJztWm1v2jAQ/isVnzqpm8JbgX2jbNW6rq3UdtOkUkUmMSEi2NR2RlHFf5/tODgJSUaAFl"
    "j5QsP5zrl7fL57bPpSGmEbevTTPQTWAJLS56OXEgIjyB+SQydHJTAe6wEhYKDnSV0WUepR"
    "RoDFuLgPPAq5yIbUIu6YuRhxKfI9TwixxRVd5GiRj9wnH5oMO5AF3jw8crGLbPgMafh1PD"
    "T7LvTsmLOuLd4t5SabjqXsArFzqSje1jMt7PkjpJXHUzbAaK7tIiakDkSQAAbF9Iz4wn3h"
    "nQo0jCjwVKsELkZsbNgHvsci4S6JgYWRwI97Q2WAjnjLx0q51qg1q6e1JleRnswljVkQno"
    "49MJQIXN+XZnIcMBBoSBg1bvLvAnKdASDp0IX6CfC4y0nwQqjy0AsFGj6dMhvCbwSeTQ8i"
    "hw3417Jh5KD1q33b+da+PeZaH0Q0mKdxkN7XaqgSjAlINYTASUEwM/eU9r+Tb0fw20j+Rc"
    "CybQIpLZJyEZND1mkgLQv7QdYsDaQ2OQA5B3IMKJ1gktI/spGM2rxzKEVH7g8jvUUIesAa"
    "TgCxzdiIxpznIaEwpQqcKcPzy1voARniIsSKmHTkJG8KdqnrN3t92PUbwOiJ516l69eh0S"
    "wttQSzMI9CqeILEkRcwVkoLg6NKqOkBCDeWmz1bvGmOEwpzE4DmE3sLK1z4HU711f/O16X"
    "2GD1mmEvt7Xi1a1Sry9R3bhWZnWTY/FGoc44ZqGUjBttmfWtWb42kbML7WIB30VwzzGBro"
    "Mu4VRifMGdAshKS9fFI+u+YJvVGriYgMm8MCbyiYfOA4Ys2Nztu077y9fSLLsDr9ln9FpR"
    "5ttQuL6wWFcATe+x+Fxyse6CqVZZrBWLNF+qeu/0lC9Vvdzv+i3DaIWL12yerr9gMjAz0W"
    "wjYRJBbaBtprEhTORKDOE0ArNa7fk6qdHATg2yAcG+M4ha6d6dmidcbia74iyXSoQxpHCJ"
    "SHjZZIJGlA5sYo/YBEW4AHBKe/vNLtjl9Wq/8XYNLna0nBQ7VU524UApcbNEdWwa5Z0hX/"
    "vLZ+stu7pjTNbyAC1GYyMW7+nmMoetCkQ2QFU7aprdw29ZRhpJja3R0cz7pMJsdPVLpX0i"
    "ozrKJBeNEfs4GY3RzSQXjTPV9cmohDefjcqtk3atpbZUzqVWqHEgoTtWcPNI6P5SgEYV2v"
    "wTgkZABPhzq29slQ6sdG2ffeovcm+/xoF/e13vVa/o25C41iCtlqmR3GoGtM6hnu1RPfsD"
    "CVUbZdmSFjHZz58dX+U4I7ZGARCV+n4C+Co/gfM3Mpj2vwTf726uMw6E2iQB5E/EA3ywXY"
    "udHHkuZY+7CWsOiiJq4fSI0icvCt7xVft3EtfOj5sziQKmzCFyFjnBWbEmu/n2MvsL8dbF"
    "Dg=="
)
