
resource null_resource "invoke-azure-cli" {
  provisioner "local-exec" {
    command = <<EOF
./az login --service-principal --username=$ARM_CLIENT_ID --password=$ARM_CLIENT_SECRET --tenant=$ARM_TENANT_ID
./az graph query -q "project id, name, type, location, tags"
EOF
    environment = {
      AZURE_CORE_COLLECT_TELEMETRY = "0"
    }
  }
}



