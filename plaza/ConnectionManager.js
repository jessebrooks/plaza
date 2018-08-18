module.exports=function(){

    this.dbConnections = [];

    this.dbConnections["plaza-mysql"] = {
            host: process.env.EndPoint_rdsPlazaMysql,
            port: process.env.Port_rdsPlazaMysql,
            user: process.env.User_rdsPlazaMysql,
            password: process.env.Password_rdsPlazaMysql,
            database: "plaza",
        };
    };