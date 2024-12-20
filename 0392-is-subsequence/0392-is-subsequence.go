func isSubsequence(s string, t string) bool {
    var S,T int
    S=len(s)
    T=len(t)
    if  S>T{
        return false
    }
    if S==0{
        return true
    }
    var j int 
    j=0
    for i:=0;i<T;i++{
        if t[i]==s[j]{
            if j==S-1{
                return true
            }
            j++
        }
    }
    return false 

    
}