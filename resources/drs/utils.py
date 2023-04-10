# Endpoint URL
endpoint_url = "http://localhost:5000/ga4gh/drs/v1/objects/{object_id}"



DRS_SCHEMA = {
    "type" : "object",
    "properties" : {
        "id" : {"type" : "string"},
        "name" : {"type" : "string"},
        "self_uri" : {"type" : "string"},
        "size" : {"type" : "number"},
        "created_time" : {"type" : "string"},
        "updated_time" : {"type" : "string"},
        "version" : {"type" : "string"},
        "mime_type" : {"type" : "string"},
        "description" : {"type" : "string"},
        "checksums": {"type" : "array"},
        "access_methods": {"type" : "array"},
        "aliases": {"type" : "array"},
        "contents": {"type" : "array"}
    },
    "required": ["id", "self_uri", "size", "created_time", "checksums"]
}

SUCCESS_STATUS_OBJECTS = ["8e18bfb64168994489bc9e7fda0acd4f","ecbb0b5131051c41f1c302287c13495c"]
FAILURE_STATUS_OBJECTS = ["xx18bfb64168994489bc9e7fda0acd4f"]
DRS_OBJECTS = SUCCESS_STATUS_OBJECTS + FAILURE_STATUS_OBJECTS