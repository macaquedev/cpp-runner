/*
ID: macaquedev
LANG: C++11
TASK: test
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
            os << ", "" << v[i] << '"';        
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
    ifstream cin("test.in");
    ofstream cout("test.out");
    
    
    
    return 0;
}