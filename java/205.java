public class Solution {
    public boolean isIsomorphic(String s, String t) {
        int[] keys = new int[512];
        for (int i = 0; i < s.length(); i++){
          //如果当前一组字符的上一次出现位置不一样，则证明不能替换
          if (keys[s.charAt(i)] != keys[t.charAt(i)+256]){
            return false;
          }
          //更新当前出现的一组字符的最后出现位置
          //int默认初始化为0，所以这里i+1，可以是最小为1，避免和默认冲突
          keys[s.charAt(i)] = keys[t.charAt(i)] = i+1;
        }
        return true;
    }
}
