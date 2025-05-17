import java.util.Arrays;

class Solution {
    public boolean solution(String[] phone_book) {
        int n = phone_book.length;
        Arrays.sort(phone_book);
        
        for (int i = 0; i < n - 1; i++) {
            if (phone_book[i].startsWith(phone_book[i + 1])) return false;
            if (phone_book[i + 1].startsWith(phone_book[i])) return false;
        }
        
        return true;
    }
}