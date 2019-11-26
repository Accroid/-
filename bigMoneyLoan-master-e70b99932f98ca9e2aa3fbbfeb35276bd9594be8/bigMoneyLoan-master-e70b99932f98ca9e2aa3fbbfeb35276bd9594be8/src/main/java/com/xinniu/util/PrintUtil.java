package com.xinniu.util;

import com.alibaba.fastjson.JSONObject;
import org.apache.commons.lang3.builder.ReflectionToStringBuilder;
import org.apache.commons.lang3.builder.ToStringBuilder;
import org.apache.commons.lang3.builder.ToStringStyle;

import static org.fusesource.jansi.Ansi.Color.*;
import static org.fusesource.jansi.Ansi.ansi;

/**
 * Created by sunjinghai on 2018/6/8.
 */
public class PrintUtil {
    public static final String RED_C = "RED";
    public static final String YELLOW_C = "YELLOW";
    public static final String GREEN_C = "GREEN";
    public static final String BLUE_C = "BLUE";
    public static final String CYAN_C = "CYAN";
    public static final String MAGENTA_C = "MAGENTA";


    public static String printObject(Object obj) {
        if (obj == null)
            return null;
        return ToStringBuilder.reflectionToString(obj, ToStringStyle.SHORT_PREFIX_STYLE);
    }

    public static void printG(Object string) {
        printColor(string, GREEN_C);
    }

    public static void printY(Object string) {
        printColor(string, YELLOW_C);
    }

    public static void printR(Object string) {
        printColor(string, RED_C);
    }

    public static void printB(Object string) {
        printColor(string, BLUE_C);
    }
    public static void printC(Object string) {
        printColor(string, CYAN_C);
    }
    public static void printM(Object string) {
        printColor(string, MAGENTA_C);
    }

    public static void printColor(Object object, String color) {
        if (object == null)
            return;
        if (color == null) {
            color = "DEFAULT";
            return;
        }
        String string = "";
        if (!(object instanceof String) && !(object instanceof JSONObject)) {
            string = ToStringBuilder.reflectionToString(object, ToStringStyle.SHORT_PREFIX_STYLE);

        }else if(object instanceof JSONObject){
            string = ((JSONObject) object).toJSONString();
        }else{
            string = (String) object;
        }

        switch (color) {
            case RED_C:
                System.out.println(ansi().eraseScreen().fg(RED).a(string).reset());
                break;
            case YELLOW_C:
                System.out.println(ansi().eraseScreen().fg(YELLOW).a(string).reset());
                break;
            case GREEN_C:
                System.out.println(ansi().eraseScreen().fg(GREEN).a(string).reset());
                break;
            case BLUE_C:
                System.out.println(ansi().eraseScreen().fg(BLUE).a(string).reset());
                break;
            case CYAN_C:
                System.out.println(ansi().eraseScreen().fg(CYAN).a(string).reset());
                break;
            case MAGENTA_C:
                System.out.println(ansi().eraseScreen().fg(MAGENTA).a(string).reset());
                break;
            default:
                System.out.println(ansi().eraseScreen().fg(GREEN).a(string).reset());
                break;
        }
    }
}
