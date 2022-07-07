# 2185. Counting Words With a Given Prefix

Easy

You are given an array of strings ```words``` and a string ```pref```.

Return the number of strings in ```words``` that contain ```pref``` as a **prefix**.

A **prefix** of a string ```s``` is any leading contiguous substring of ```s```.

**Example 1:**

<pre>
<strong>Input:</strong> words = ["pay","<strong>at</strong>tention","practice","<strong>at</strong>tend"], pref = "at"
<strong>Output:</strong> 2
<strong>Explanation:</strong> The 2 strings that contain "at" as a prefix are: "<strong>at</strong>tention" and "<strong>at</strong>tend".
</pre>

**Example 2:**

<pre>
<strong>Input:</strong> words = ["leetcode","win","loops","success"], pref = "code"
<strong>Output:</strong> 0
<strong>Explanation:</strong> There are no strings that contain "code" as a prefix.
</pre>

**Constraints:**

- ```1 <= words.length <= 100```
- ```1 <= words[i].length, pref.length <= 100```
- ```words[i]``` and ```pref``` consist of lowercase English letters.
