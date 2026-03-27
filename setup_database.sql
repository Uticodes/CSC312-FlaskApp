-- ============================================================
--  MIVA-CSC312 | Flask App Database Setup Script
--  Run this in your MySQL client (e.g. MySQL Workbench or CLI)
-- ============================================================

-- Step 1: Create the database
CREATE DATABASE IF NOT EXISTS flask_app_db;

-- Step 2: Select the database
USE flask_app_db;

-- Step 3: Create the tbl_user table
CREATE TABLE IF NOT EXISTS tbl_user (
    id          INT          NOT NULL AUTO_INCREMENT,
    username    VARCHAR(100) NOT NULL UNIQUE,
    password    VARCHAR(255) NOT NULL,          -- Stores the hashed password
    created_at  TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

-- ============================================================
--  Verify: Show the table structure
-- ============================================================
DESCRIBE tbl_user;

-- ============================================================
--  Optional: View all registered users (run after signing up)
-- ============================================================
-- SELECT id, username, created_at FROM tbl_user;