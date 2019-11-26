package com.xinniu.util;

import java.io.Serializable;

/**
 * Created by sunjinghai on 2018/12/6.
 */
public class TestDataDTO implements Serializable{
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public String getCaseId() {
        return caseId;
    }

    public void setCaseId(String caseId) {
        this.caseId = caseId;
    }

    public String getCaseName() {
        return caseName;
    }

    public void setCaseName(String caseName) {
        this.caseName = caseName;
    }

    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }

    public String getParams() {
        return params;
    }

    public void setParams(String params) {
        this.params = params;
    }

    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }

    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }

    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }



    @Override
    public String toString() {
        return "TestDataDTO{" +
                "url='" + url + '\'' +
                ", caseId='" + caseId + '\'' +
                ", caseName='" + caseName + '\'' +
                ", method='" + method + '\'' +
                ", params='" + params + '\'' +
                ", body='" + body + '\'' +
                ", code='" + code + '\'' +
                ", message='" + message + '\'' +
                ", clientType='" + clientType + '\'' +
                ", result='" + result + '\'' +
                ", status='" + status + '\'' +
                '}';
    }

    private String url;
    private String caseId;
    private String caseName;
    private String method;
    private String params;
    private String body;
    private String code;
    private String message;
    private String clientType;
    private String result;
    private String status;


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }


    public String getResult() {
        return result;
    }

    public void setResult(String result) {
        this.result = result;
    }



    public String getClientType() {
        return clientType;
    }

    public void setClientType(String clientType) {
        this.clientType = clientType;
    }
}
