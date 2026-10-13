
class new_node:
    def __init__(self,url:str):
        self.url=url
        self.next=None
        self.prev=None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage=new_node(homepage)
        self.curr=self.homepage
        

    def visit(self, url: str) -> None:
        new_page=new_node(url)
        self.curr.next=new_page
        new_page.prev=self.curr
        self.curr=self.curr.next
        
        

    def back(self, steps: int) -> str:
        while self.curr.prev!=None and steps>0:
            self.curr=self.curr.prev
            steps-=1
        return self.curr.url    
        

    def forward(self, steps: int) -> str:
        while self.curr.next!=None and steps>0:
            self.curr=self.curr.next
            steps-=1
        return self.curr.url    
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)