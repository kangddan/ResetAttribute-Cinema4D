import c4d

def psr(obj):
    obj.SetRelPos(c4d.Vector(0,0,0))
    obj.SetRelScale(c4d.Vector(1,1,1))
    obj.SetRelRot(c4d.Vector(0,0,0))

def resetUsetData(obj):
    userData = obj.GetUserDataContainer()
    if not userData: return

    for descId, container in userData:
        defaultValue = container[c4d.DESC_DEFAULT]
        if defaultValue is None:
            continue
        obj[descId] = defaultValue

def main():
    sel = doc.GetSelection()
    if not sel:
        return

    doc.StartUndo()
    for obj in sel:
        if not isinstance(obj, c4d.BaseObject):
            continue
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)
        psr(obj)
        resetUsetData(obj)   
    doc.EndUndo()
    c4d.EventAdd()  
      
if __name__ == '__main__':
    main()
        
        