use android_app;

CREATE TABLE Log (
	userid varchar(50) NULL,
	label varchar(50) NULL,
	location varchar(50) NULL,
	latitude FLOAT NULL,
	longitude FLOAT NULL,
	createtime DATETIME NULL,
	modifytime DATETIME NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8
COLLATE=utf8_general_ci;

CREATE TABLE APIAuth (
	`key` mediumblob NULL,
	createtime DATETIME NULL,
	modifytime DATETIME NULL
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8
COLLATE=utf8_general_ci;
