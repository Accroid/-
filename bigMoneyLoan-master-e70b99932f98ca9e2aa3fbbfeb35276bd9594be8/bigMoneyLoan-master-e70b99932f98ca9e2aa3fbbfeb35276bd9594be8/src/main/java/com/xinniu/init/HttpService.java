package com.xinniu.init;

import com.alibaba.fastjson.JSON;
import com.alibaba.fastjson.JSONObject;
import com.google.common.collect.Multimap;
import com.xinniu.util.PrintUtil;
import okhttp3.*;
import org.apache.commons.lang3.StringUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.context.annotation.Bean;
import org.springframework.stereotype.Service;

import java.io.File;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.net.URLEncoder;
import java.util.Collection;
import java.util.Map;
import java.util.concurrent.TimeUnit;


/**
 * Created by sunjinghai on 2018/6/8.
 */
@Service
public class HttpService {

    private static final Logger logger = LoggerFactory.getLogger(HttpService.class);

    private OkHttpClient client = new OkHttpClient()
            .newBuilder().readTimeout(60,TimeUnit.SECONDS).build();
    //json文本
    public static final MediaType APPLICATION_JSON = MediaType.parse("application/json; charset=utf-8");
    public static final MediaType PROTOBUF = MediaType.parse("application/x-protobuf; charset=utf-8");
//    public static final MediaType FORMDATR = MediaType.parse("application/x-www-form-urlencoded; charset=utf-8");
//    public static final MediaType APPLICATION_JSON = MediaType.parse("application/x-www-form-urlencoded; charset=utf-8");


    //普通文本
    public static final MediaType TEXT_PLAIN = MediaType.parse("text/plain");

    public Response doGet(Request request) {
        if (request == null) {
            logger.error("request is null!");
            return null;
        }
        PrintUtil.printB(request);
        Response response = null;
        try {
            Long beginTime=System.currentTimeMillis();
            response = client.newCall(request).execute();
            Long endTime = System.currentTimeMillis();
            PrintUtil.printC("耗时:"+(endTime-beginTime));

        } catch (IOException e) {
            e.printStackTrace();
        }
        if (response != null) {
            logger.warn(response.toString());
        }
        return response;
    }

    public Response doGet(String url) {
        Request request = new Request.Builder().url(url).build();
        return doGet(request);
    }

    public Response doGet(String url, Map<String, Object> body) {
        url = url + "?";
        for (String key : body.keySet()) {
            url = url + key + "=" + body.get(key) + "&";
        }
        url = url.substring(0, url.length() - 1);
        Request request = new Request.Builder().url(url).build();
        return doGet(request);
    }

    public Response doGet(String url, String body) {
        Map<String, Object> mapBody = (Map) JSON.parse(body);
        url = url + "?";
        for (String key : mapBody.keySet()) {
            url = url + key + "=" + mapBody.get(key) + "&";
        }
        url = url.substring(0, url.length() - 1);
        Request request = new Request.Builder().url(url).build();
        return doGet(request);
    }

//    public Response doGet(String url, Map<String, String> singleHeaders, Multimap<String, String> multiHeaders) {
//        Request.Builder builder = new Request.Builder();
//        Request request = addHeader(builder, singleHeaders, multiHeaders).url(url).build();
//        return doGet(request);
//    }

    public Response doGet(String url, Multimap<String, String> headers) {
        Request request = new Request.Builder().url(url).build();
        request = addHeader(request, headers);
        return doGet(request);
    }

    public Response doGet(String url, String body, Multimap<String, String> headers) {
        Map<String, Object> mapBody = (Map) JSON.parse(body);
        url = url + "?";
        for (String key : mapBody.keySet()) {
            url = url + key + "=" + mapBody.get(key) + "&";
        }
        url = url.substring(0, url.length() - 1);
        Request request = new Request.Builder().url(url).build();
        request = addHeader(request, headers);
        return doGet(request);
    }

    public Response doGet(String url, Map<String, Object> body, Multimap<String, String> headers) {
        url = url + "?";
        for (String key : body.keySet()) {
            url = url + key + "=" + body.get(key) + "&";
        }
        url = url.substring(0, url.length() - 1);

        Request request = new Request.Builder().url(url).build();
        request = addHeader(request, headers);
        return doGet(request);
    }

    public Response doPost(Request request) {
        Response response = null;
        if (request == null) {
            return null;
        }
        PrintUtil.printB(request);
        try {
            Long beginTime=System.currentTimeMillis();
            response = client.newCall(request).execute();
            Long endTime = System.currentTimeMillis();
            PrintUtil.printC("耗时:"+(endTime-beginTime));
        } catch (IOException e) {
            e.printStackTrace();
        }
        if (response != null) {
            logger.info(response.toString());
        }
        return response;
    }

//    public Response doPost(String url) {
////        RequestBody body = RequestBody.create(APPLICATION_JSON, json);
//        Request request = new Request.Builder().url(url).post(new RequestBody() {
//            @Override
//            public MediaType contentType() {
//                return null;
//            }
//
//            @Override
//            public void writeTo(BufferedSink bufferedSink) throws IOException {
//
//            }
//        }).build();
//        return doPost(request);
//    }

    public Response doPost(String url,Map<String,Object> json) {
        FormBody.Builder builder = new FormBody.Builder();
        for (String key : json.keySet()) {
            //追加表单信息
            builder.add(key, json.get(key).toString());
        }
        RequestBody body = builder.build();
        Request request = new Request.Builder().url(url).post(body).build();
        return doPost(request);
    }

    public Response doPost(String url, String json) {
        RequestBody body = RequestBody.create(APPLICATION_JSON, json);
        Request request = new Request.Builder().url(url).post(body).build();
        return doPost(request);
    }

    public Response doPost(String url, Multimap<String, String> headers) {
        RequestBody body = RequestBody.create(APPLICATION_JSON, "");
        Request request = new Request.Builder().url(url).post(body).build();
        request = addHeader(request, headers);
        return doPost(request);
    }

    public Response doPost(String url, String json, Map<String, String> singleHeaders,
                           Multimap<String, String> multiHeaders) {
        RequestBody body = RequestBody.create(APPLICATION_JSON, json);
        Request.Builder builder = new Request.Builder();
        Request request = addHeader(builder, singleHeaders, multiHeaders).url(url).post(body).build();
        return doPost(request);
    }

    public Response doPost(String url, String json, Multimap<String, String> headers) {
        RequestBody body = RequestBody.create(APPLICATION_JSON, json);
        Request request = new Request.Builder().url(url).post(body).build();
        request = addHeader(request, headers);
        return doPost(request);
    }

    public Response doPost(String url, String json, Multimap<String, String> headers, File file) {
        RequestBody querybody = RequestBody.create(APPLICATION_JSON, json);
        RequestBody fileBody = RequestBody.create(MediaType.parse("image/png"), file);
        RequestBody body = new MultipartBody.Builder().setType(MultipartBody.FORM)
                .addFormDataPart("file", "img", fileBody)
                .addPart(querybody).build();
        Request request = new Request.Builder().url(url).post(body).build();
        request = addHeader(request, headers);
        return doPost(request);
    }

    public Response doPost(String url, Map<String, Object> param, Multimap<String, String> headers) {
        url = url + "?";
        for (String key : param.keySet()) {
            url = url + key + "=" + param.get(key) + "&";
        }
        url = url.substring(0, url.length() - 1);
        RequestBody body = RequestBody.create(APPLICATION_JSON, "");
        Request request = new Request.Builder().url(url).post(body).build();
        request = addHeader(request, headers);
        return doPost(request);
    }

    public Response doDelete(Request request){
        Response response = null;
        if (request == null) {
            return null;
        }
        PrintUtil.printB(request);
        try {
            response = client.newCall(request).execute();
        } catch (IOException e) {
            e.printStackTrace();
        }
        if (response != null) {
            logger.info(response.toString());
        }
        return response;
    }

    public Response doDelete(String url, String json) {
        RequestBody body = RequestBody.create(APPLICATION_JSON, json);
        Request request = new Request.Builder().url(url).delete(body).build();
        return doDelete(request);
    }

    public Response doDelete(String url, Multimap<String, String> headers) {
        RequestBody body = RequestBody.create(APPLICATION_JSON, "");
        Request request = new Request.Builder().url(url).delete(body).build();
        request = addHeader(request, headers);
        return doDelete(request);
    }

    public Response doDelete(String url, String json, Map<String, String> singleHeaders,
                           Multimap<String, String> multiHeaders) {
        RequestBody body = RequestBody.create(APPLICATION_JSON, json);
        Request.Builder builder = new Request.Builder();
        Request request = addHeader(builder, singleHeaders, multiHeaders).url(url).delete(body).build();
        return doDelete(request);
    }

    public Response doDelete(String url, String json, Multimap<String, String> headers) {
        RequestBody body = RequestBody.create(APPLICATION_JSON, json);
        Request request = new Request.Builder().url(url).delete(body).build();
        request = addHeader(request, headers);
        return doDelete(request);
    }

    public Response doDelete(String url, String json, Multimap<String, String> headers, File file) {
        RequestBody querybody = RequestBody.create(APPLICATION_JSON, json);
        RequestBody fileBody = RequestBody.create(MediaType.parse("image/png"), file);
        RequestBody body = new MultipartBody.Builder().setType(MultipartBody.FORM)
                .addFormDataPart("file", "img", fileBody)
                .addPart(querybody).build();
        Request request = new Request.Builder().url(url).delete(body).build();
        request = addHeader(request, headers);
        return doDelete(request);
    }

    public Response doDelete(String url, Map<String, Object> param, Multimap<String, String> headers) {
        url = url + "?";
        for (String key : param.keySet()) {
            url = url + key + "=" + param.get(key) + "&";
        }
        url = url.substring(0, url.length() - 1);
        RequestBody body = RequestBody.create(APPLICATION_JSON, "");
        Request request = new Request.Builder().url(url).delete(body).build();
        request = addHeader(request, headers);
        return doDelete(request);
    }

    public Response doPut(Request request){
        Response response = null;
        if (request == null) {
            return null;
        }
        PrintUtil.printB(request);
        try {
            response = client.newCall(request).execute();
        } catch (IOException e) {
            e.printStackTrace();
        }
        if (response != null) {
            logger.info(response.toString());
        }
        return response;
    }

    public Response doPut(String url, String json) {
        RequestBody body = RequestBody.create(APPLICATION_JSON, json);
        Request request = new Request.Builder().url(url).put(body).build();
        return doPut(request);
    }

    public Response doPut(String url, Multimap<String, String> headers) {
        RequestBody body = RequestBody.create(APPLICATION_JSON, "");
        Request request = new Request.Builder().url(url).put(body).build();
        request = addHeader(request, headers);
        return doPut(request);
    }

    public Response doPut(String url, String json, Map<String, String> singleHeaders,
                             Multimap<String, String> multiHeaders) {
        RequestBody body = RequestBody.create(APPLICATION_JSON, json);
        Request.Builder builder = new Request.Builder();
        Request request = addHeader(builder, singleHeaders, multiHeaders).url(url).put(body).build();
        return doPut(request);
    }

    public Response doPut(String url, String json, Multimap<String, String> headers) {
        RequestBody body = RequestBody.create(APPLICATION_JSON, json);
        Request request = new Request.Builder().url(url).put(body).build();
        request = addHeader(request, headers);
        return doPut(request);
    }

    public Response doPut(String url, String json, Multimap<String, String> headers, File file) {
        RequestBody querybody = RequestBody.create(APPLICATION_JSON, json);
        RequestBody fileBody = RequestBody.create(MediaType.parse("image/png"), file);
        RequestBody body = new MultipartBody.Builder().setType(MultipartBody.FORM)
                .addFormDataPart("file", "img", fileBody)
                .addPart(querybody).build();
        Request request = new Request.Builder().url(url).put(body).build();
        request = addHeader(request, headers);
        return doPut(request);
    }

    public Response doPut(String url, Map<String, Object> param, Multimap<String, String> headers) {
        url = url + "?";
        for (String key : param.keySet()) {
            url = url + key + "=" + param.get(key) + "&";
        }
        url = url.substring(0, url.length() - 1);
        RequestBody body = RequestBody.create(APPLICATION_JSON, "");
        Request request = new Request.Builder().url(url).put(body).build();
        request = addHeader(request, headers);
        return doPut(request);
    }

    public String parseResponseBody2String(Response response) {
        if (response != null) {
            if (response.isSuccessful()) {
                try {
                    return response.body().string();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
        return null;
    }

    public Request.Builder addHeader(Request.Builder builder, Map<String, String> singleHeaders,
                                     Multimap<String, String> multiHeaders) {
        if (singleHeaders != null && singleHeaders.size() > 0) {
            for (String header : singleHeaders.keySet()) {
                builder.header(header, singleHeaders.get(header));
            }
        }

        if (multiHeaders != null && multiHeaders.size() > 0) {
            for (String header : multiHeaders.keySet()) {
                Collection<String> values = multiHeaders.get(header);
                for (String value : values) {
                    builder.addHeader(header, value);
                }
            }
        }
        return builder;
    }

    public Request addHeader(Request request, Multimap<String, String> headers) {
        Request.Builder builder = request.newBuilder();

        if (headers != null && headers.size() > 0) {
            for (String header : headers.keySet()) {
                Collection<String> values = headers.get(header);
                if (values.size() > 1) {
                    for (String value : values) {
                        builder.addHeader(header, value);
                    }
                } else {
                    builder.header(header, (String) values.toArray()[0]);
                }
            }
        }
        return builder.build();
    }

    public String buildUrl(String url, Map<String, String> query) {

        HttpUrl.Builder builder = new HttpUrl.Builder();

        if (query != null && query.size() > 0) {
            for (String key : query.keySet()) {
                builder.addQueryParameter(key, query.get(key));
            }
        }
        return builder.build().toString();
    }

    public String buildUrl(String scheme, String host, Integer port, String path, Map<String, String> query) {
        if (StringUtils.isBlank(scheme)) {
            scheme = "http";
        }
        if (StringUtils.isBlank(host)) {
            host = "localhost";
        }
        if (StringUtils.isBlank(path)) {
            path = "";
        }

        HttpUrl.Builder builder = new HttpUrl.Builder()
                .scheme(scheme)
                .host(host);

        String[] paths = path.split("/");
        for (String p : paths) {
            builder.addPathSegment(p);
        }

        if (port != null) {
            builder.port(port.intValue());
        }
        if (query != null && query.size() > 0) {
            for (String key : query.keySet()) {
                builder.addQueryParameter(key, query.get(key));
            }
        }
        return builder.build().toString();
    }

    public String buildUrlWithEncode(String scheme, String host, Integer port, String path, Map<String, String> query) {
        if (StringUtils.isBlank(scheme)) {
            scheme = "http";
        }
        if (StringUtils.isBlank(host)) {
            host = "localhost";
        }
        if (StringUtils.isBlank(path)) {
            path = "";
        }

        HttpUrl.Builder builder = new HttpUrl.Builder()
                .scheme(scheme)
                .host(host);

        String[] paths = path.split("/");
        for (String p : paths) {
            builder.addPathSegment(p);
        }

        if (port != null) {
            builder.port(port.intValue());
        }
        if (query != null && query.size() > 0) {
            for (String key : query.keySet()) {
                try {
                    builder.addEncodedQueryParameter(
                            URLEncoder.encode(key, "utf-8"), URLEncoder.encode(query.get(key), "utf-8"));
                } catch (UnsupportedEncodingException e) {
                    e.printStackTrace();
                }
            }
        }
        return builder.build().toString();
    }
//
//    public void https() {
//        ConnectionSpec spec = new ConnectionSpec.Builder(ConnectionSpec.MODERN_TLS)
//                .tlsVersions(TlsVersion.TLS_1_2)
//                .cipherSuites(
//                        CipherSuite.TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256,
//                        CipherSuite.TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256,
//                        CipherSuite.TLS_DHE_RSA_WITH_AES_128_GCM_SHA256)
//                .build();
//
//        client.setConnectionSpecs(Collections.singletonList(spec));
//    }
}
