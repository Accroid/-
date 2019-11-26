package com.xinniu.init;

import org.omg.CORBA.Environment;

import java.io.File;

/**
 * Created by sunjinghai on 2018/6/12.
 */
public class ComConstants {
    public static final int CODE = 0;
    public static final Boolean SUCCESS = true;

    public static final File FACE_PHOTO = new File(Environment.class.getResource("/").getFile()+"face.jpeg");
    public static final File BACK_PHOTO = new File(Environment.class.getResource("/").getFile()+"back.jpeg");
    public static final File HOLD_PHOTO = new File(Environment.class.getResource("/").getFile()+"hold.jpeg");

}
