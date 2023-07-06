

;刷新DNS
~>!d::
{
    Run, D:\.tools\made\dns.exe
    return
}

;speach
~>!r::
{
    send ^c
    Sleep, 600
    PostMessage, 0x100, 82, 1, , ahk_exe speach.exe
    return
}
;quit

~!q::
{
    if GetKeyState("w", "P")
    {
        run D:\.tools\MLbats\shut.pyw
    }
    
        Return
}
;web
<#w::
{
    run,C:\Program Files\Google\Chrome\Application\chrome.exe
    Return
}

;webs
~>!s::
{
    Run, D:\.tools\made\python\python\dist\assist2\runtime.exe
    Return
}

<#o::
{
    run,D:\.tools\UmiOCR\extra\ocr.pyw
}