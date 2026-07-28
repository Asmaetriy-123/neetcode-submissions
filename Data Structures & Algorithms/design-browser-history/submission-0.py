class Page:
    def __init__(self,url):
        self.url=url
        self.next=None
        self.prev=None

class BrowserHistory:

    def __init__(self, homepage: str):
        homepage=Page(homepage)
        self.head=homepage
        self.tail=homepage
        self.current=homepage
        

    def visit(self, url: str) -> None:
        new_page=Page(url)
        self.current.next=new_page
        new_page.prev=self.current
        self.current=new_page
        self.tail=new_page

        

    def back(self, steps: int) -> str:
       
        while steps > 0 and self.current.prev:
               self.current = self.current.prev
               steps -= 1
        return self.current.url 

        

    def forward(self, steps: int) -> str:

        while steps > 0 and self.current.next:
            self.current = self.current.next
            steps -= 1
        return self.current.url 



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)