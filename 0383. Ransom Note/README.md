# 383. Ransom Note

Easy

Given two strings <pre>ransomNote</pre> and <pre>magazine</pre>, return <pre>true</pre> if <pre>ransomNote</pre> can be constructed by using the letters from <pre>magazine</pre> and <pre>false</pre> otherwise.

Each letter in <pre>magazine</pre> can only be used once in <pre>ransomNote</pre>.

Example 1:

<pre>
Input: ransomNote = "a", magazine = "b"
Output: false
</pre> 

Example 2:

<pre>
Input: ransomNote = "aa", magazine = "ab"
Output: false
</pre> 

Example 3:

<pre>
Input: ransomNote = "aa", magazine = "aab"
Output: true
</pre> 

Constraints:

- <pre>1 <= ransomNote.length, magazine.length <= 105</pre>
- <pre>ransomNote</pre> and <pre>magazine</pre> consist of lowercase English letters.
