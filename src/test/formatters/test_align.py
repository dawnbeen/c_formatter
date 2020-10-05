# ############################################################################ #
#                                                                              #
#                                                         :::      ::::::::    #
#    test_align.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: cacharle <me@cacharle.xyz>                 +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/10/04 12:19:45 by cacharle          #+#    #+#              #
#    Updated: 2020/10/04 14:57:52 by cacharle         ###   ########.fr        #
#                                                                              #
# ############################################################################ #

from formatters.align import align, align_scope, align_local


def test_align_global_basic():
    output = """\
int\t\tfoo()
char\tbar()
"""

    assert output == align_scope("""\
int foo()
char   bar()
""", scope="global")
    assert output == align_scope("""\
int\t\t\t\t\t\tfoo()
char   bar()
""", scope="global")
    assert output == align_scope("""\
int\t\t\t         \t\t\tfoo()
char  \t bar()
""", scope="global")
    assert output == align_scope("""\
int\t\t\t         \t\t\tfoo()
char  \t bar()
""", scope="global")


def test_align_local_basic():
    output = """
{
\tint\t\tfoo;
\tchar\tbar;
}
"""

    assert output == align_local("""
{
\tint foo;
\tchar   bar;
}
""")
    assert output == align_local("""
{
\tint\t\t\t\t\t\tfoo;
\tchar   bar;
}
""")
    assert output == align_local("""
{
\tint\t\t\t         \t\t\tfoo;
\tchar  \t bar;
}
""")
    assert output == align_local("""
{
\tint\t\t\t         \t\t\tfoo;
\tchar  \t bar;
}
""")


def test_align_global_prototypes_basic():
    input = """
int                      a();
int   b();
int \t\t\t\tc();
int\t\t\t\t d();
int   e();
int \t\t\t\t\t\tf();
int \t\tg();
char    a();
char          b();
char    c();
char d();
char\t\t\t\te();
char\tf();
char\t\t\t\t\t\t\tg();
uint64_t\t\t\t\t\ta();
uint64_t  b();
uint64_t c();
uint64_t\t\t\t\t\t\t\t\t\t\td();
uint64_t\t\t\t\t\t\t\t\t\t\t\te();
uint64_t                  f();
uint64_t\tg();
"""
    output = """
int\t\t\ta();
int\t\t\tb();
int\t\t\tc();
int\t\t\td();
int\t\t\te();
int\t\t\tf();
int\t\t\tg();
char\t\ta();
char\t\tb();
char\t\tc();
char\t\td();
char\t\te();
char\t\tf();
char\t\tg();
uint64_t\ta();
uint64_t\tb();
uint64_t\tc();
uint64_t\td();
uint64_t\te();
uint64_t\tf();
uint64_t\tg();
"""
    assert align(input) == output


def test_align_local_multiple_functions():
    input = """
int\t\t\t\t\t\t\t\t\t\tf()
{
\tint a = 0;
}
int\t\t\t              g()
{
\tint a;
\tint    b;
\tint           a;
\tint                a;
\tchar   a;
}
char\t\t\t\t\t\t\t\t\ta()
{
\tint                                                        a;
\tint    b;
\tint           a;
\tint                a;
\tchar   a;
\tuint64_t              a;
}
char\t\t\t\tf()
{
\tt_very_looooooooooooooooooooooooooooooooooooooooooooooong yo;
\tint i;
}
char g()
{
}
uint64_t   a()
{
}
uint64_t\t\t\tb()
{
}
"""
    output = """
int\t\t\tf()
{
\tint a = 0;
}
int\t\t\tg()
{
\tint\t\ta;
\tint\t\tb;
\tint\t\ta;
\tint\t\ta;
\tchar\ta;
}
char\t\ta()
{
\tint\t\t\ta;
\tint\t\t\tb;
\tint\t\t\ta;
\tint\t\t\ta;
\tchar\t\ta;
\tuint64_t\ta;
}
char\t\tf()
{
\tt_very_looooooooooooooooooooooooooooooooooooooooooooooong\tyo;
\tint\t\t\t\t\t\t\t\t\t\t\t\t\t\t\ti;
}
char\t\tg()
{
}
uint64_t\ta()
{
}
uint64_t\tb()
{
}
"""
    assert align(input) == output


def test_align_prototypes_type_spaces():
    input = """
unsigned foo();
unsigned int foo();
long foo();
long long foo();
long long int foo();
static long long int foo();
static short short int foo();
static short int foo();
"""
    output = """
unsigned\t\t\t\tfoo();
unsigned int\t\t\tfoo();
long\t\t\t\t\tfoo();
long long\t\t\t\tfoo();
long long int\t\t\tfoo();
static long long int\tfoo();
static short short int\tfoo();
static short int\t\tfoo();
"""
    assert align(input) == output


def test_align_local_type_spaces():
    input = """
int qq()
{
\tunsigned foo;
\tunsigned int foo;
\tlong foo;
\tlong long foo;
\tlong long int foo;
\tstatic long long int foo;
\tstatic short short int foo;
\tstatic short int foo;
\tregister long long int foo;
\tvolatile short short int foo;
}
"""
    output = """
int\tqq()
{
\tunsigned\t\t\t\t\tfoo;
\tunsigned int\t\t\t\tfoo;
\tlong\t\t\t\t\t\tfoo;
\tlong long\t\t\t\t\tfoo;
\tlong long int\t\t\t\tfoo;
\tstatic long long int\t\tfoo;
\tstatic short short int\t\tfoo;
\tstatic short int\t\t\tfoo;
\tregister long long int\t\tfoo;
\tvolatile short short int\tfoo;
}
"""
    assert align(input) == output


def test_align_local_type_array():
    input = """
int qq()
{
\tunsigned foo[2];
\tunsigned int foo[2][2];
\tlong foo[BUFFER_SIZE];
\tlong long foo[A][B][C];
\tlong long int foo[A][B][C];
\tstatic long long int foo[A][B][C][A][B][C][A][B][C][A][B][C][A][B][C][A][B][C][A][B][C][A][B][C];
\tstatic short short int foo[1][2][3][1][2][3][1][2][3][1][2][3][1][2][3][1][2][3][1][2][3][1][2][3];
\tregister long long int foo[10000000000000000000000000000000000000000];
\tvolatile short short int foo[AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA];
}
"""
    output = """
int\tqq()
{
\tunsigned\t\t\t\t\tfoo[2];
\tunsigned int\t\t\t\tfoo[2][2];
\tlong\t\t\t\t\t\tfoo[BUFFER_SIZE];
\tlong long\t\t\t\t\tfoo[A][B][C];
\tlong long int\t\t\t\tfoo[A][B][C];
\tstatic long long int\t\tfoo[A][B][C][A][B][C][A][B][C][A][B][C][A][B][C][A][B][C][A][B][C][A][B][C];
\tstatic short short int\t\tfoo[1][2][3][1][2][3][1][2][3][1][2][3][1][2][3][1][2][3][1][2][3][1][2][3];
\tregister long long int\t\tfoo[10000000000000000000000000000000000000000];
\tvolatile short short int\tfoo[AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA];
}
"""
    assert align(input) == output


def test_align_ptr_type():
    input = """
int *ptr()
{
\tint *a;
\tint ******a;
\tint *****************a;
\tchar *****************a;
}
int ***********ptr();
char ***********ptr(char ********************a);
uint64_t ***********ptr(char ********************a);
"""
    output = """
int\t\t\t*ptr()
{
\tint\t\t*a;
\tint\t\t******a;
\tint\t\t*****************a;
\tchar\t*****************a;
}
int\t\t\t***********ptr();
char\t\t***********ptr(char ********************a);
uint64_t\t***********ptr(char ********************a);
"""
    assert align(input) == output


def test_align_function_ptr():
    input = """
int qa()
{
\tint (*func)(int a, int b);
\tint (*func2)(int, int);
\tvoid (*func2)(int, int);
\tunsigned long long int (*func2)();
\tunsigned long long int (*func2)(void*);
\tunsigned long long int (*func2)(void**********);
}
"""
    output = """
int\tqa()
{
\tint\t\t\t\t\t\t(*func)(int a, int b);
\tint\t\t\t\t\t\t(*func2)(int, int);
\tvoid\t\t\t\t\t(*func2)(int, int);
\tunsigned long long int\t(*func2)();
\tunsigned long long int\t(*func2)(void*);
\tunsigned long long int\t(*func2)(void**********);
}
"""
    assert align(input) == output


def test_align_function_ptr_array():
    input = """
int qa()
{
\tint (*func[2])(int a, int b);
\tint (*func2[A])(int, int);
\tvoid (*func2[11111111111110000000000000000000])(int, int);
\tunsigned long long int (*func2[aaaaaaaaaaaaaaaaaaaaaaaaaa])();
}
"""
    output = """
int\tqa()
{
\tint\t\t\t\t\t\t(*func[2])(int a, int b);
\tint\t\t\t\t\t\t(*func2[A])(int, int);
\tvoid\t\t\t\t\t(*func2[11111111111110000000000000000000])(int, int);
\tunsigned long long int\t(*func2[aaaaaaaaaaaaaaaaaaaaaaaaaa])();
}
"""
    assert align(input) == output