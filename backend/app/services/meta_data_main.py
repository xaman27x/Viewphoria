from fastapi import APIRouter, HTTPException
from app.services.metadata_extractor.parquet import get_metadata_parquet
from app.services.metadata_extractor.iceberg import get_metadata_iceberg
from pydantic import BaseModel, Field
from typing import Literal, Union
from datetime import datetime

class MetadataRequestAWS(BaseModel):
    file_type: Literal["parquet", "iceberg", "delta", "hudi"]
    file_path: str = Field(..., pattern=r"^s3://[a-zA-Z0-9./_-]+$")
    is_protected: bool
    iam_access_id: str
    iam_secret_access_key: str
    region_name: str
    bucket_name: str

class MetadataResponse(BaseModel):
    metadata: Union[dict, list]
    status: int
    server_timestamp: datetime

async def get_metadata(request: MetadataRequestAWS):
    try:
        params = {
            "file_type": request.file_type,
            "file_path": request.file_path,
            "is_protected": request.is_protected,
            "region_name": request.region_name,
            "bucket_name": request.bucket_name,
            "iam_access_id": request.iam_access_id,
            "iam_secret_access_key": request.iam_secret_access_key
        }
        metadata = []
        if request.file_type == "parquet":
            unified_metadata_parquet = get_metadata_parquet(aws_access_key_id=params["iam_access_id"], aws_secret_access_key=params["iam_secret_access_key"], region_name=params["region_name"], bucket_name=params["bucket_name"])
            return MetadataResponse(
                metadata=unified_metadata_parquet,
                status=200,
                server_timestamp=datetime.now()
            )
        
        elif request.file_type == "iceberg":
            unified_metadata_iceberg = get_metadata_iceberg(aws_access_key_id=params['iam_access_id'], aws_secret_access_key=params["iam_secret_access_key"], region_name=params["region_name"], bucket_name=params["bucket_name"])
            return MetadataResponse(
                metadata=unified_metadata_iceberg,
                status=200,
                server_timestamp=datetime.now()
            )
        
        else:
            return []
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))
