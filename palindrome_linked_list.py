#234.palindrome deque사용하지 않고 풀어보기

#rev는 slow가 중간에 도달할때까지의 값을 뒤집어준 값이 들어감
rev = None
slow = fast = head

#fast는 두칸씩 slow는 한칸씩 fast가 끝에 다다르면 slow는 node의 중간에 도달
while fast and fast.next:
    fast = fast.next.next
    #revnext에는 rev값을, rev에는 slow값을, slow에는 slow.next값을
    rev, rev.next, slow = slow, rev, slow.next

#fast가 값이 있으면 node가 홀수로 slow는 비교가 불필요한 중간값에 있으므로 next로 옮겨줌
if fast:
    slow = slow.next

#rev와 val의 값을 하나씩 비교
while rev and rev.val == slow.val:
    slow, rev = slow.next, rev.next

#rev가 none이면 true반환, rev가 값이 있으면 false 반환
print(not rev)