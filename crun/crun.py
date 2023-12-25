import os
import argparse

home = os.path.expanduser("~")
template = """#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mk make_pair
#define pii pair<int, int>
#define vi vector<int>
#define vpii vector<pii>
#define vs vector<string>
#define all(x) (x).begin(), (x).end()
#define umap unordered_map
#define uset unordered_set
#define MOD 1000000007
#define imax INT_MAX
#define imin INT_MIN
#define exp 1e9
#define sz(x) (int((x).size()))
#define elif else if


template<typename T, typename Y>
auto operator<<(std::ostream& os, const std::pair<T,Y>& p) -> std::ostream&
{
    os << '(';
    if (typeid(T) == typeid(string)) {
        os << '"' << p.first << '"';
    }
    else {
        os << p.first;
    }
    os << ", ";
    if (typeid(Y) == typeid(string)) {
        os << '"' << p.second << '"';
    }
    else {
        os << p.second;
    }
    os << ')';
    return os;
}

template<typename T>
auto operator<<(std::ostream& os, const std::vector<T>& v) -> std::ostream&
{
    os << "[";
    if (v.size() == 0) {
        os << "]";
        return os;
    }
    if (typeid(T) == typeid(string)) {
        os << '"' << v[0] << '"';
    }
    else {
        os << v[0];
    }
    for (int i=1; i<v.size(); i++) {
        if (typeid(T) == typeid(string)) {
            os << ", \"" << v[i] << '"';        
        }
        else {
            os << ", " << v[i];
        }
    }
    os << "]";
    return os;
}

template<typename T>
auto operator<<(std::ostream& os, const std::set<T>& s) -> std::ostream&
{
    if (s.size() == 0) {
        os << "{}";
        return os;
    }
    os << "{";
    
    int i=0;

    for (auto value : s) {
        if (i++ != 0) os << ", ";
        if (typeid(T) == typeid(string)) os << '"' << value << '"';
        else os << value;
    }
    os << "}";
    return os; 
}

template<typename T>
auto operator<<(std::ostream& os, const std::unordered_set<T>& s) -> std::ostream&
{
    if (s.size() == 0) {
        os << "{}";
        return os;
    }
    os << "{";
    
    int i=0;

    for (auto value : s) {
        if (i++ != 0) os << ", ";
        if (typeid(T) == typeid(string)) os << '"' << value << '"';
        else os << value;
    }
    os << "}";
    return os; 
}

template<typename T, typename Y>
auto operator<<(std::ostream& os, const std::map<T, Y>& m) -> std::ostream&
{
    if (m.size() == 0) {
        os << "{}";
        return os;
    }
    os << "{";
    
    int i=0;

    for (auto [key, value] : m) {
        if (i++ != 0) os << ", ";
        if (typeid(T) == typeid(string)) os << '"' << key << '"';
        else os << key;
        os << ": ";
        if (typeid(Y) == typeid(string)) os << '"' << value << '"';
        else os << value;
    }
    os << "}";
    return os; 
}  

template<typename T, typename Y> 
auto operator<<(std::ostream& os, const std::unordered_map<T, Y>&  m) -> std::ostream&
{
    if (m.size() == 0) {
        os << "{}";
        return os;
    }
    os << "{";
    
    int i=0;

    for (auto [key, value] : m) {
        if (i++ != 0) os << ", ";
        if (typeid(T) == typeid(string)) os << '"' << key << '"';
        else os << key;
        os << ": ";
        if (typeid(Y) == typeid(string)) os << '"' << value << '"';
        else os << value;
    }
    os << "}";
    return os; 
}

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int ttt; cin >> ttt;
    while(ttt--) {
        
    }
    return 0;
}"""

usaco_template = """/*
ID: %s
LANG: C++11
TASK: %s
*/
#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define pb push_back
#define mk make_pair
#define pii pair<int, int>
#define vi vector<int>
#define vpii vector<pii>
#define vs vector<string>
#define all(x) (x).begin(), (x).end()
#define umap unordered_map
#define uset unordered_set
#define MOD 1000000007
#define imax INT_MAX
#define imin INT_MIN
#define exp 1e9
#define sz(x) (int((x).size()))
#define elif else if


template<typename T, typename Y>
auto operator<<(std::ostream& os, const std::pair<T,Y>& p) -> std::ostream&
{
    os << '(';
    if (typeid(T) == typeid(string)) {
        os << '"' << p.first << '"';
    }
    else {
        os << p.first;
    }
    os << ", ";
    if (typeid(Y) == typeid(string)) {
        os << '"' << p.second << '"';
    }
    else {
        os << p.second;
    }
    os << ')';
    return os;
}

template<typename T>
auto operator<<(std::ostream& os, const std::vector<T>& v) -> std::ostream&
{
    os << "[";
    if (v.size() == 0) {
        os << "]";
        return os;
    }
    if (typeid(T) == typeid(string)) {
        os << '"' << v[0] << '"';
    }
    else {
        os << v[0];
    }
    for (int i=1; i<v.size(); i++) {
        if (typeid(T) == typeid(string)) {
            os << ", \"" << v[i] << '"';        
        }
        else {
            os << ", " << v[i];
        }
    }
    os << "]";
    return os;
}

template<typename T>
auto operator<<(std::ostream& os, const std::set<T>& s) -> std::ostream&
{
    if (s.size() == 0) {
        os << "{}";
        return os;
    }
    os << "{";
    
    int i=0;

    for (auto value : s) {
        if (i++ != 0) os << ", ";
        if (typeid(T) == typeid(string)) os << '"' << value << '"';
        else os << value;
    }
    os << "}";
    return os; 
}

template<typename T>
auto operator<<(std::ostream& os, const std::unordered_set<T>& s) -> std::ostream&
{
    if (s.size() == 0) {
        os << "{}";
        return os;
    }
    os << "{";
    
    int i=0;

    for (auto value : s) {
        if (i++ != 0) os << ", ";
        if (typeid(T) == typeid(string)) os << '"' << value << '"';
        else os << value;
    }
    os << "}";
    return os; 
}

template<typename T, typename Y>
auto operator<<(std::ostream& os, const std::map<T, Y>& m) -> std::ostream&
{
    if (m.size() == 0) {
        os << "{}";
        return os;
    }
    os << "{";
    
    int i=0;

    for (auto [key, value] : m) {
        if (i++ != 0) os << ", ";
        if (typeid(T) == typeid(string)) os << '"' << key << '"';
        else os << key;
        os << ": ";
        if (typeid(Y) == typeid(string)) os << '"' << value << '"';
        else os << value;
    }
    os << "}";
    return os; 
}  

template<typename T, typename Y> 
auto operator<<(std::ostream& os, const std::unordered_map<T, Y>&  m) -> std::ostream&
{
    if (m.size() == 0) {
        os << "{}";
        return os;
    }
    os << "{";
    
    int i=0;

    for (auto [key, value] : m) {
        if (i++ != 0) os << ", ";
        if (typeid(T) == typeid(string)) os << '"' << key << '"';
        else os << key;
        os << ": ";
        if (typeid(Y) == typeid(string)) os << '"' << value << '"';
        else os << value;
    }
    os << "}";
    return os; 
}
int32_t main()
{
    ifstream cin("%s.in");
    ofstream cout("%s.out");
    
    
    
    return 0;
}"""


def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="file to run")
    parser.add_argument("-u", "--usaco", help="use usaco template", action="store_true")
    args = parser.parse_args()
    if not os.path.exists(f"{args.filename}.cpp"):
        with open(f"{args.filename}.cpp", "w+") as f:
            if args.usaco:
                if os.path.exists(os.path.join(home, ".usaco")):
                    with open(os.path.join(home, ".usaco")) as f2:
                        username = f2.readline().strip()
                else:
                    username = input("Please enter your usaco username: ")
                    with open(os.path.join(home, ".usaco"), "w+") as f2:
                        f2.write(username)

                f.write(usaco_template % (username, args.filename, args.filename, args.filename))
            else:
                f.write(template)
    else:
        with open(f"{args.filename}.cpp") as f:
            data = f.readlines()

        with open("a.cpp", "w+") as f:
            for i in range(len(data)):
                data[i] = data[i].replace(f'ifstream cin("{args.filename}.in");', '')
                data[i] = data[i].replace(f'ofstream cout("{args.filename}.out");', '')
                data[i] = data[i].replace('ios_base::sync_with_stdio(false);', '')
                data[i] = data[i].replace('cin.tie(NULL);', '')
                print(data[i])
            f.writelines(data)

        os.system(f"g++ a.cpp")
        os.system(f"./a.out")
        os.system(f"rm -rf ./a.out")
        os.system(f"rm -rf ./a.cpp")


if __name__ == "__main__":
    cli()