def emplyeeOutput(emplyee):
    print("<<급여관리 프로그램>>\n")
    print("사번\t" "급수\t" "호\t" "수당\t" "지급액\t" "세금\t" "차인지급액\t")
    print(f"{emplyee['snum']}\t {emplyee['gub']}\t {emplyee['ho']}\t {emplyee['salary']:,}\t {emplyee['gigub']:,}\t {emplyee['segum']}\t {emplyee['chain']:,}\t" )
 
    