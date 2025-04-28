$BasePath = "C:\Users\peg0252\"

$FolderName = "DeleteMe"


if (Test-Path -Path $BasePath\$FolderName) {
    "Path Exists"
    $answer = Read-Host "Would you like to Delete the path? Yes Or No: "

    if ($answer -eq 'Yes') {
        Remove-Item -Path $BasePath\$FolderName
        "Folder Has been Removed"
    }
} else {
    "Path Doeses not exist"
    #New-Item -Path $BasePath -Name $FolderName
    $answer = Read-Host "Would you like to Delete the path? Yes Or No: "

    if ($answer -eq 'Yes') {
        Remove-Item -Path $BasePath\$FolderName
        "Folder Has been Removed"
    }
}

