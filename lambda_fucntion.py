import json
import boto3

client = boto3.client("dynamodb")

def lambda_handler(event, context):
    return VisitorCount()

def VisitorCount():
    # Scan the table to get the current visitor count
    response = client.scan(TableName="VisitorCount")

    if "Items" in response and len(response["Items"]) > 0:
        # Save the response (JSON)
        count = int(response["Items"][0]["visitor_count"]["N"])
    else:
        count = 0
    count += 1

    # Update the visitor count in the table
    update_response = client.update_item(
        TableName="VisitorCount",
        Key={
            "id": {
                "S": "visitor_count_id",  # Match the partition key name and value exactly
            },
        },
        ExpressionAttributeNames={
            "#VC": "visitor_count"
        },
        ExpressionAttributeValues={
            ":count": {
                "N": str(count),
            },
        },
        UpdateExpression="SET #VC = :count",
        ReturnValues="ALL_NEW"
    )

    return {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Content-Type": "application/json"
        },
        "body": json.dumps({"visitor_count": count})
    }