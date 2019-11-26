package com.xinniu.common;

import com.xinniu.util.PrintUtil;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.test.context.ContextConfiguration;

import java.sql.*;

/**
 * Created by sunjinghai on 2018/6/21.
 */
@Configuration
@PropertySource(value = "classpath:environmentInit.properties")
@ContextConfiguration("classpath:/spring.xml")
public class Database {

    public static void action(String sql) throws SQLException, ClassNotFoundException, IllegalAccessException, InstantiationException {
        Class.forName("com.mysql.cj.jdbc.Driver");
        String url = "jdbc:mysql://115.231.223.139:9902/bitan_otc?useUnicode=true&characterEncoding=UTF-8&useSSL=false&autoReconnect=true";
        String username = "root";
        String password = "otc2018";
        Connection con = DriverManager.getConnection(url, username, password);
        Statement stat = con.createStatement();
        stat.executeUpdate(sql);
        stat.close();
        con.close();
    }

    public static String sqlCustomerGetData(String sql) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
        String url = "jdbc:mysql://192.168.4.10:3306/csp?useUnicode=true&characterEncoding=UTF-8&useSSL=false&autoReconnect=true";
//        String username = "mpm_test";
//        String password = "mpm@t#";
        String username = "cspread";
        String password = "jhk4#f";
        Connection con = null;
        try {
            con = DriverManager.getConnection(url, username, password);
            Statement stat = con.createStatement();
            ResultSet resultSet = stat.executeQuery(sql);
            resultSet.next();
            String resultData = resultSet.getString(1);
            stat.close();
            con.close();
            PrintUtil.printC(sql);
            PrintUtil.printC(resultData);
            return resultData;
        } catch (SQLException e) {
            e.printStackTrace();
            return null;
        }

    }

    public static String sqlUserGetData(String sql) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
        String url = "jdbc:mysql://192.168.4.10:3306/app-ceshi-db?useUnicode=true&characterEncoding=UTF-8&useSSL=false&autoReconnect=true";
        String username = "mpm_test";
        String password = "mpm@t#";
//        String username = "cspread";
//        String password = "jhk4#f";
        Connection con = null;
        try {
            con = DriverManager.getConnection(url, username, password);
            Statement stat = con.createStatement();
            ResultSet resultSet = stat.executeQuery(sql);
            resultSet.next();
            String resultData = resultSet.getString(1);
            stat.close();
            con.close();
            PrintUtil.printC(sql);
            PrintUtil.printC(resultData);
            return resultData;
        } catch (SQLException e) {
            e.printStackTrace();
            return null;
        }

    }
}
