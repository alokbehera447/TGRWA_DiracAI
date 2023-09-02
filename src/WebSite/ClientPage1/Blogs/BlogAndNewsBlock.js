import classes from "./BlogAndNewsBlock.module.css";
import bookAppointment from "./bookAppointment.jpg";
import bn1 from "./bn1.jpg";
import bn2 from "./bn2.jpg";
import bn3 from "./bn3.jpg";
import bn4 from "./bn4.jpg";
import SingleBlog from "../../Home/SingleBlog";



import BlogImage1 from './BlogImage1.png';
import BlogImage2 from './BlogImage2.png';
import BlogImage3 from './BlogImage3.png';
import BlogImage4 from './BlogImage4.png';










function BlogAndNewsBlock() {


    let title1="Everything You Need To Know About RERA Odisha";
   let text1="The emergence of the Real Estate Regulatory Authority brought a paradigm shift in the realty sector of Odisha. There were many conflicts between the buyers and sellers of real estate in the past  ...";
   let link1="https://www.squareyards.com/blog/rera-odisha-rerat";




   let title4="Housing Society Byelaws & Member Rights";
   let text4="A housing society meeting may not appeal to you, especially if petty matters are discussed. It can be exhausting knowing your water pump will be fixed or when your sinking fund will be used. It is crucial ...";
   let link4="https://vakilsearch.com/blog/housing-society-byelaws-member-rights/";

   let title2="All You Need To Know About Society Maintenance Charges";
   let text2="Once you are the rightful owner of a residence in a housing society, you are part of a larger, more inclusive, white picket fence community. Homeownership is not only a matter of pride and joy but a lifelong";
   let link2="https://mygate.com/blog/cooperative-housing-society/society-maintenance-charges/";


   let title3="Apartment Pet Policies: A Comprehensive Guide to Rules and Regulations";
   let text3="When it comes to apartment hunting, pet owners face a unique set of challenges. Finding a place that accommodates furry family members can be a     ";
   let link3="https://adda.io/blog/2023/04/apartment-pet-policies/";









  return (
    <div className={classes.blogAndNewsContainer}>
      <div className={classes.latest}>
        <div className={classes.latestTitle}>Blogs</div>
        <div className={classes.latestsubTitle}>Latest Posts</div>
      </div>

      <div className={classes.newsContainer}>


        <SingleBlog title={title1} text={text1} link={link1} image={BlogImage1}/>
        <SingleBlog title={title2} text={text2} link={link2} image={BlogImage2}/>
        <SingleBlog title={title3} text={text3} link={link3} image={BlogImage3}/>
        <SingleBlog title={title4} text={text4} link={link4} image={BlogImage4}/>


      </div>
    </div>
  );
}

export default BlogAndNewsBlock;
