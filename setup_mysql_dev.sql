-- Dev database
CREATE USER IF NOT EXISTS 'pld_admin'@'localhost' IDENTIFIED BY 'admin_pwd';
CREATE DATABASE IF NOT EXISTS pld_admin_db;
GRANT ALL PRIVILEGES ON `pld_admin_db`.* TO 'pld_admin'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'pld_admin'@'localhost';

USE pld_admin_db;
-- CREATE TABLE posts (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     title VARCHAR(255) NOT NULL,
--     content TEXT NOT NULL,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- INSERT INTO posts (title, content) VALUES 
-- ('First Blog Post', 'This is the content of the first blog post. You can add the details of your blog here.'),
-- ('Second Blog Post', 'This is the content of the second blog post. Your blog content will be here.'),
-- ('Third Blog Post', 'This is the content of the third blog post. You can add your blog posts here.');
