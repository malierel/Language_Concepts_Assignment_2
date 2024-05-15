; Reverse List
(define (reverse-list lst)
  (if (null? lst)
      '()
      (append (reverse-list (cdr lst)) (list (car lst)))))

; Remove Duplicates
(define (remove-duplicates lst)
  (define (helper lst seen)
    (cond ((null? lst) '())
          ((member (car lst) seen) (helper (cdr lst) seen))
          (else (cons (car lst) (helper (cdr lst) (cons (car lst) seen))))))
  (helper lst '()))

; Concatenate Lists
(define (concatenate-lists lst1 lst2)
  (append lst1 lst2))

; List Intersection
(define (list-intersection lst1 lst2)
  (define (intersect-helper lst1 lst2)
    (cond ((null? lst1) '())
          ((member (car lst1) lst2)
           (cons (car lst1) (intersect-helper (cdr lst1) lst2)))
          (else (intersect-helper (cdr lst1) lst2))))
  (intersect-helper lst1 lst2))

; Testing the functions
(display (reverse-list '(1 2 3 4)))            ; Output: (4 3 2 1)
(newline)
(display (remove-duplicates '(1 2 2 3 4 4)))   ; Output: (1 2 3 4)
(newline)
(display (concatenate-lists '(1 2) '(3 4)))    ; Output: (1 2 3 4)
(newline)
(display (list-intersection '(1 2 3 4) '(2 4 6))) ; Output: (2 4)
(newline)
